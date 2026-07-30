# OrthoReg 36-run formal comparison: data summary

## Cohort and balance

- 36 completed formal phantom runs: 18 Adaptive and 18 Fixed k=10.
- 3 pseudonymous operators (12 runs each), 2 Vision Pro devices (18 runs each), 2 anatomies, and 3 held-out TRE groups.
- Each run contains seven held-out TRE measurements, yielding 252 formal TRE observations.
- The design is prospective and balanced, but no random allocation record exists; it must not be described as randomized.
- Two preliminary model-off exports are documented separately and excluded from every formal table and archive.

## Primary result

- Adaptive run-level TRE RMSE: 1.008 +/- 0.111 mm.
- Fixed k=10 run-level TRE RMSE: 2.458 +/- 0.438 mm.
- Adjusted Adaptive-minus-Fixed effect: -1.450 mm (HC3 95% CI -1.682 to -1.218 mm).
- All seven TRE points were <=3 mm in 18/18 Adaptive runs and 3/18 Fixed runs (two-sided Fisher p=2.93e-07).

## Acquisition and mechanism

- Adaptive median stop count: 11 points (range 10-15); 16/18 stopped at k=10 or 11.
- Adaptive used 0.89 more points on average than Fixed k=10.
- Mean registration-point bounding-box diagonal increased by 60.76 mm.
- Mean pairwise distance increased by 25.41 mm.
- Translation and rotation uncertainty decreased by 7.36 mm and 2.15 degrees, respectively.

## Workflow cost

- Registration acquisition duration was 54.2 s for Adaptive and 23.3 s for Fixed k=10.
- These data support accuracy, reliability, and spatial-information gains under a sparse point budget; they do not support a speed advantage over Fixed k=10.

## Data-quality status

- 36 unique planned packages matched one-to-one to complete exports.
- Protocol, anatomy, and TRE-group mismatches: 0.
- Transform-freeze records before held-out TRE: 36/36.
- Formal TRE rows after excluding the two preliminary exports: 252/252 expected.
- Sequence 32 is retained because its current exported attempt is complete; earlier interrupted attempts were not exported.

## Repository publication note

- The source-faithful `workflow_events_public.csv` contains one exact duplicated
  `excel_tre_group_selected` planning event. Deduplicate exact rows before using
  the table for event-frequency analysis.
