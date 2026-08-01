# Public metadata package

This directory contains the final public metadata supplement for the prospective OrthoReg-World Adaptive stop-and-complete study:

- [`TMI_OrthoRegWorld_Online_Adaptive_Metadata.zip`](TMI_OrthoRegWorld_Online_Adaptive_Metadata.zip)
- SHA-256: `c8087af23dee9fd6a98c64f08ca411db6bfa8c08a0a277c65e29a99ab57fdfcc`

## Scope

The archive contains exactly 18 formal Adaptive sessions from 18 physical HMD acquisition sessions. It does not contain the 18 Fixed-k=10 comparison packages, the constrained-randomization schedule, source code, raw frames, video, screenshots, depth data, or other pixel-bearing content.

The package is therefore not a complete export of the separate 36-run Adaptive-versus-Fixed comparison reported in the manuscript.

## Contents

The extracted archive contains session metadata, source-faithful audit tables, analysis-support tables, schema documentation, a checksum inventory, QC reports, and `scripts/verify_no_frames.py`. The package contains 967 files in total.

Device identity was absent from the source package and is recorded as `NA`; it must not be inferred from session identifiers.

## TRE endpoint handling

The manuscript endpoint is target-registration-error root-mean-square error (TRE RMSE). It is not point-cloud RMSE.

Raw audit records intentionally preserve duplicate or measurement-invalid TRE observations in two sessions. The analysis-support tables provide the manuscript-aligned endpoint based on the latest unique valid observation per target. Use those endpoint fields together with the supplied QC flags; retain the raw rows for auditability.

## Verification

From the repository root:

```bash
shasum -a 256 -c MANIFEST_SHA256.txt
unzip data/TMI_OrthoRegWorld_Online_Adaptive_Metadata.zip
cd TMI_OrthoRegWorld_Online_Adaptive_Metadata
python3 scripts/verify_no_frames.py . --expected-sessions 18
```

The expected verifier result is `passed: true`, with 18 sessions and no frame-like or pixel-bearing files detected.
