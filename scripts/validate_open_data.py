#!/usr/bin/env python3
"""Validate the public OrthoReg-World 36-run phantom dataset."""

from __future__ import annotations

import csv
import json
import math
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_csv(relative_path: str) -> list[dict[str, str]]:
    path = ROOT / relative_path
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"PASS  {label}")


def require_count(rows: list[dict[str, str]], expected: int, label: str) -> None:
    require(len(rows) == expected, f"{label}: {len(rows)} rows (expected {expected})")


def unique_count(rows: list[dict[str, str]], key: str) -> int:
    return len({row[key] for row in rows})


def require_nonempty(
    rows: list[dict[str, str]], keys: list[str], label: str
) -> None:
    missing = {
        key: sum(not row[key].strip() for row in rows)
        for key in keys
        if any(not row[key].strip() for row in rows)
    }
    require(not missing, f"{label} required fields are populated: {missing}")


def exact_duplicate_count(rows: list[dict[str, str]]) -> int:
    if not rows:
        return 0
    fields = tuple(rows[0].keys())
    fingerprints = [tuple(row[field] for field in fields) for row in rows]
    return len(fingerprints) - len(set(fingerprints))


def numeric_mean(rows: list[dict[str, str]], key: str) -> float:
    return statistics.fmean(float(row[key]) for row in rows)


def scan_public_data(paths: list[Path]) -> list[str]:
    patterns = {
        "email address": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
        "local user path": re.compile(r"(?:/Users/|[A-Z]:\\Users\\)", re.I),
        "web URL": re.compile(r"https?://", re.I),
        "private IPv4 address": re.compile(
            r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|"
            r"192\.168\.\d{1,3}\.\d{1,3}|"
            r"172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b"
        ),
        "credential-like assignment": re.compile(
            r"\b(?:api[_-]?key|password|bearer|secret)\b\s*[:=]", re.I
        ),
    }

    matches: list[str] = []
    for path in paths:
        text = path.read_text(encoding="utf-8-sig")
        for label, pattern in patterns.items():
            if pattern.search(text):
                matches.append(f"{path.relative_to(ROOT)}: {label}")
    return matches


def main() -> int:
    required_files = [
        "data/run_level_public.csv",
        "data/tre_point_level_public.csv",
        "data/workflow_events_public.csv",
        "data/quality_warnings_public.csv",
        "analysis/reproduced_headline_statistics.json",
        "metadata/data_dictionary.csv",
        "metadata/device_mapping.csv",
    ]
    for relative_path in required_files:
        require((ROOT / relative_path).is_file(), f"required file exists: {relative_path}")

    runs = read_csv("data/run_level_public.csv")
    points = read_csv("data/tre_point_level_public.csv")
    events = read_csv("data/workflow_events_public.csv")
    warnings = read_csv("data/quality_warnings_public.csv")

    require_count(runs, 36, "formal run table")
    require_count(points, 252, "held-out TRE point table")
    require_count(events, 1725, "workflow event table")
    require_count(warnings, 200, "quality-warning table")
    require_nonempty(
        runs,
        [
            "package_name",
            "trial_id",
            "protocol",
            "operator_id",
            "apple_vision_pro_id",
            "anatomy",
            "tre_group_id",
            "analysis_status",
            "stop_k",
            "tre_rmse_mm",
            "tre_points_n",
        ],
        "run table",
    )
    require_nonempty(
        points,
        [
            "package_name",
            "trial_id",
            "landmark_index",
            "error_mm",
            "passed",
            "protocol",
            "operator_id",
            "apple_vision_pro_id",
            "anatomy",
            "tre_group_id",
        ],
        "TRE point table",
    )
    require_nonempty(
        events,
        ["package_name", "trial_id", "timestamp", "step", "action", "payload"],
        "workflow event table",
    )
    require_nonempty(
        warnings,
        ["package_name", "warning", "count"],
        "quality-warning table",
    )
    require(unique_count(runs, "trial_id") == 36, "trial_id is unique at run grain")
    require(unique_count(runs, "package_name") == 36, "package_name is unique at run grain")
    require(exact_duplicate_count(runs) == 0, "run table has no exact duplicate rows")
    require(exact_duplicate_count(points) == 0, "TRE point table has no exact duplicate rows")
    event_duplicate_rows = exact_duplicate_count(events)
    require(
        event_duplicate_rows == 1,
        "workflow event table retains the one documented duplicate planning event",
    )
    print(
        "NOTE  Deduplicate workflow events before event-frequency analysis; "
        "the source-faithful public table retains one exact duplicate row."
    )

    expected_balance = {
        "protocol": {"Adaptive": 18, "Fixed k=10": 18},
        "operator_id": {"OP-01": 12, "OP-02": 12, "OP-03": 12},
        "apple_vision_pro_id": {"VP-A": 18, "VP-B": 18},
        "anatomy": {"Tibia": 18, "Femur": 18},
        "tre_group_id": {"TRE_GROUP_1": 12, "TRE_GROUP_2": 12, "TRE_GROUP_3": 12},
    }
    for key, expected in expected_balance.items():
        actual = dict(Counter(row[key] for row in runs))
        require(actual == expected, f"balanced {key}: {actual}")

    require(
        all(row["analysis_status"] == "included" for row in runs),
        "all formal runs have analysis_status=included",
    )
    require(all(int(row["tre_points_n"]) == 7 for row in runs), "run table reports 7 TRE points")
    require(
        all(float(row["tre_rmse_mm"]) >= 0 for row in runs),
        "run-level TRE RMSE values are non-negative",
    )

    run_trial_ids = {row["trial_id"] for row in runs}
    run_packages = {row["package_name"] for row in runs}
    points_per_trial = Counter(row["trial_id"] for row in points)
    point_keys = {(row["trial_id"], row["landmark_index"]) for row in points}
    require(
        len(point_keys) == len(points),
        "(trial_id, landmark_index) is unique at TRE point grain",
    )
    require(set(points_per_trial) == run_trial_ids, "TRE table covers exactly the 36 formal trials")
    require(
        set(points_per_trial.values()) == {7},
        "every formal trial has exactly 7 held-out TRE rows",
    )
    require(
        {row["package_name"] for row in points} == run_packages,
        "TRE point table covers exactly the 36 formal packages",
    )
    require(
        all(float(row["error_mm"]) >= 0 for row in points),
        "point-level TRE errors are non-negative",
    )
    require(
        all(
            (row["passed"].lower() == "true") == (float(row["error_mm"]) <= 3.0)
            for row in points
        ),
        "point-level pass labels agree with the 3-mm threshold",
    )

    event_trials = {row["trial_id"] for row in events}
    require(event_trials == run_trial_ids, "workflow events cover exactly the 36 formal trials")
    warning_packages = {row["package_name"] for row in warnings}
    require(warning_packages == run_packages, "quality warnings cover exactly the 36 packages")
    require(
        all(int(row["count"]) >= 0 for row in warnings),
        "quality-warning counts are non-negative",
    )
    warning_keys = {(row["package_name"], row["warning"]) for row in warnings}
    require(
        len(warning_keys) == len(warnings),
        "(package_name, warning) is unique in the quality-warning table",
    )

    adaptive = [row for row in runs if row["protocol"] == "Adaptive"]
    fixed = [row for row in runs if row["protocol"] == "Fixed k=10"]
    adaptive_mean = numeric_mean(adaptive, "tre_rmse_mm")
    fixed_mean = numeric_mean(fixed, "tre_rmse_mm")
    adaptive_complete = sum(row["all_7_tre_within_3mm"].lower() == "true" for row in adaptive)
    fixed_complete = sum(row["all_7_tre_within_3mm"].lower() == "true" for row in fixed)

    with (ROOT / "analysis/reproduced_headline_statistics.json").open(
        "r", encoding="utf-8"
    ) as handle:
        headline = json.load(handle)

    require(
        math.isclose(adaptive_mean, headline["adaptive_tre_rmse_mean_mm"], abs_tol=1e-12),
        f"Adaptive TRE RMSE mean agrees with release: {adaptive_mean:.6f} mm",
    )
    require(
        math.isclose(fixed_mean, headline["fixed_tre_rmse_mean_mm"], abs_tol=1e-12),
        f"Fixed k=10 TRE RMSE mean agrees with release: {fixed_mean:.6f} mm",
    )
    require(adaptive_complete == 18, "Adaptive complete-run 3-mm reliability is 18/18")
    require(fixed_complete == 3, "Fixed k=10 complete-run 3-mm reliability is 3/18")

    scan_paths = [
        *sorted((ROOT / "data").glob("*.csv")),
        *sorted((ROOT / "analysis").glob("*.csv")),
        *sorted((ROOT / "analysis").glob("*.json")),
        *sorted((ROOT / "metadata").glob("*.csv")),
    ]
    sensitive_matches = scan_public_data(scan_paths)
    require(not sensitive_matches, f"public data sensitive-pattern scan: {sensitive_matches}")

    print("\nValidated release summary")
    print(json.dumps({
        "formal_runs": len(runs),
        "tre_points": len(points),
        "workflow_events": len(events),
        "adaptive_tre_rmse_mean_mm": round(adaptive_mean, 6),
        "fixed_tre_rmse_mean_mm": round(fixed_mean, 6),
        "adaptive_complete_3mm_runs": adaptive_complete,
        "fixed_complete_3mm_runs": fixed_complete,
    }, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, ValueError, OSError, csv.Error, json.JSONDecodeError) as exc:
        print(f"FAIL  {exc}", file=sys.stderr)
        raise SystemExit(1)
