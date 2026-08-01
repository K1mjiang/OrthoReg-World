# OrthoReg-World

An Imaging-Grounded Online World Model for Adaptive Mixed-Reality Orthopedic Registration

[中文说明](README_CN.md) · [Workflow video](https://youtu.be/YVuVoCD0BBM) · [Download public metadata](data/TMI_OrthoRegWorld_Online_Adaptive_Metadata.zip)

![Status](https://img.shields.io/badge/status-research%20prototype-6f42c1)
![Public data](https://img.shields.io/badge/public%20data-18%20Adaptive%20sessions-0b7fab)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-green)

<p align="center">
  <a href="https://youtu.be/YVuVoCD0BBM">
    <img src="assets/demo-overview.jpg" alt="OrthoReg-World workflow demonstration on Apple Vision Pro" width="900">
  </a>
</p>

<p align="center">
  <a href="https://youtu.be/YVuVoCD0BBM"><strong>▶ Play the full workflow video on YouTube</strong></a>
</p>

> GitHub does not render an embedded YouTube player in README files. The preview image and play link therefore open the video on YouTube.

## Overview

OrthoReg-World is a research prototype for adaptive mixed-reality orthopedic registration on Apple Vision Pro. The system maintains an imaging-grounded online world model, evaluates registration quality during acquisition, and determines when the currently observed evidence is sufficient. The demonstration shows femur and tibia registration followed by visualization of total-knee-arthroplasty resection planes.

This repository is a public project and data page. Enterprise API integration, application source code, deployment credentials, raw camera frames, and patient data are not included.

## Manuscript-aligned evidence

The manuscript reports two related but distinct studies. Their scopes should not be merged.

### Prospective Adaptive stop-and-complete study

- 18 physical HMD acquisition sessions using the Adaptive protocol.
- The public ZIP in this repository contains de-identified, non-pixel metadata for these 18 sessions.
- Audit records preserve source QC information, including duplicate or measurement-invalid TRE rows in two sessions.

### Constrained-randomized Adaptive-versus-Fixed comparison

- 36 formal runs: 18 Adaptive and 18 Fixed-k=10.
- Three operators, two Vision Pro devices, femur and tibia anatomy, and three held-out target-layout groups.
- A frozen, prespecified constrained-randomization schedule assigned one protocol to each operator–device–anatomy–layout cell before acquisition.
- Each run used seven held-out targets; 252 held-out target errors were analyzed.

The prespecified run-level endpoint was the seven-target target-registration-error root-mean-square error (**TRE RMSE**). It is not point-cloud RMSE or another registration residual.

| Manuscript result | Adaptive | Fixed-k=10 |
| --- | ---: | ---: |
| Runs | 18 | 18 |
| Mean TRE RMSE | 1.01 ± 0.11 mm | 2.46 ± 0.44 mm |
| Runs with all 7 targets ≤ 3 mm | 18/18 | 3/18 |

The adjusted Adaptive-minus-Fixed difference was **−1.45 mm** with an HC3 95% confidence interval of **−1.68 to −1.22 mm**.

These values are manuscript results. The downloadable ZIP is the separate 18-session Adaptive metadata supplement and does **not** contain the Fixed-k comparison packages or the constrained-randomization schedule. See [Manuscript–data alignment](docs/manuscript-data-alignment.md).

## Public metadata package

[Download `TMI_OrthoRegWorld_Online_Adaptive_Metadata.zip`](data/TMI_OrthoRegWorld_Online_Adaptive_Metadata.zip)

The package contains exactly 18 formal Adaptive sessions and their de-identified metadata, audit tables, analysis-support tables, schema documentation, checksums, and a non-pixel verification script.

| Package property | Value |
| --- | ---: |
| Physical acquisition sessions | 18 |
| Protocol | Adaptive only |
| Files in extracted package | 967 |
| Raw images, video, depth, screenshots, or pixel data | None |
| Device identifier in source package | Not available (`NA`) |

### Important endpoint note

The package preserves source-faithful raw audit rows. Consequently, raw session-summary TRE fields can include a duplicated or measurement-invalid observation. For manuscript-aligned session endpoints, use the analysis-support fields based on the latest unique valid observation per target and retain the supplied QC flags. Do not silently discard the raw audit trail or interpret a flagged raw summary as the final endpoint.

### Verify the download

From the repository root:

```bash
shasum -a 256 -c MANIFEST_SHA256.txt
unzip data/TMI_OrthoRegWorld_Online_Adaptive_Metadata.zip
cd TMI_OrthoRegWorld_Online_Adaptive_Metadata
python3 scripts/verify_no_frames.py . --expected-sessions 18
```

The included verifier checks the manifest, session count, checksum inventory, and absence of frame-like or pixel-bearing files.

## Repository structure

```text
OrthoReg-World/
├── README.md
├── README_CN.md
├── LICENSE
├── MANIFEST_SHA256.txt
├── SECURITY.md
├── assets/
│   └── demo-overview.jpg
├── data/
│   ├── README.md
│   └── TMI_OrthoRegWorld_Online_Adaptive_Metadata.zip
└── docs/
    ├── data-availability-statement.txt
    └── manuscript-data-alignment.md
```

## Intended use and limitations

OrthoReg-World is a research prototype evaluated in controlled phantom experiments. It is not a medical device, is not approved for clinical decision-making, and must not be used for patient care. Public metadata do not expose private application code or licensed enterprise services.

## Citation

Until a formal publication record is available, please cite the project as:

```text
Jiang K, Fan W, Shi H, Hu L, Lin Z, Zeng B, Chen X.
OrthoReg-World: An Imaging-Grounded Online World Model for Adaptive
Mixed-Reality Orthopedic Registration. Research project and public
metadata supplement, 2026.
https://github.com/K1mjiang/OrthoReg-World
```

## License

The public repository materials and metadata supplement are released under the [Creative Commons Attribution 4.0 International License](LICENSE). Third-party software, services, and trademarks remain subject to their respective terms.
