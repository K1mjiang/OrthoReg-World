# Manuscript–data alignment

This note defines how statements in this repository map to the OrthoReg-World manuscript and the downloadable metadata package.

## Two distinct evidence sets

| Evidence set | Manuscript role | Size | Public ZIP coverage |
| --- | --- | ---: | --- |
| Prospective Adaptive stop-and-complete study | Evaluates the online stopping policy and dense completion within the Adaptive workflow | 18 physical HMD sessions | Complete de-identified non-pixel metadata for all 18 sessions |
| Constrained-randomized Adaptive-versus-Fixed comparison | Compares Adaptive with Fixed-k=10 across operator, device, anatomy, and target-layout cells | 36 runs: 18 Adaptive and 18 Fixed-k=10 | Not included in this ZIP |

The 18 sessions in the public ZIP must not be described as the Adaptive half of the 36-run comparison unless a session-level provenance mapping establishes that relationship. No such mapping is asserted by this release.

## Randomization statement

The manuscript describes the formal 36-run Adaptive-versus-Fixed experiment as a **prospective constrained-randomized comparison**. A frozen, prespecified constrained-randomization schedule assigned a protocol to every operator–device–anatomy–layout cell before acquisition, and all 36 retained packages conformed to that schedule.

Accordingly, repository descriptions should consistently preserve the manuscript's constrained-randomized design statement. The schedule itself is outside the downloadable 18-session Adaptive metadata package.

## Public-data statement

The accurate current statement is:

> A workflow video and de-identified non-pixel metadata for the 18 prospective Adaptive stop-and-complete sessions are publicly available in this repository. The 18 Fixed-k=10 comparison packages and constrained-randomization schedule are not included in the downloadable metadata archive.

Manuscript results from the 36-run comparison may be summarized on the project page, but they must be identified as manuscript results rather than as values recomputed from the public ZIP.

## Endpoint definition

The prespecified comparison endpoint is the seven-target **TRE RMSE**, where TRE means target registration error. It is not point-cloud RMSE, fitting RMSE, or a generic registration residual.

The public 18-session package retains source-faithful audit rows. Duplicate or measurement-invalid TRE rows in two sessions remain visible for traceability. Manuscript-aligned endpoints use the latest unique valid observation for each target together with the supplied QC flags.

## Repository wording rules

- Describe the 36-run formal comparison as constrained-randomized.
- Describe the downloadable ZIP as an 18-session Adaptive metadata supplement.
- Do not claim that Fixed-k=10 run packages are included in the ZIP.
- Do not claim that the comparison schedule is included in the ZIP.
- Label reported 36-run statistics as manuscript results.
- Use `TRE RMSE` when naming the endpoint.
