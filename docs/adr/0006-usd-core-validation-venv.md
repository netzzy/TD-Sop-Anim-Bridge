# ADR 0006 — usd-core validation in an isolated venv

Status: Accepted

## Context

We author `.usda` by hand (see [0002](0002-self-written-usda.md)), so we need an
independent way to confirm the output is valid USD and internally coherent. TD's
Python has no `pxr`, and adding USD into the TD process is risky.

## Decision

Keep a separate virtualenv `tools/.venv-usd` with `usd-core` installed, used purely
as an out-of-process checker. `tools/validate_usd.py` opens the `.usda`, traverses
the geometry prim, and for every authored time code asserts element-count coherence:
positions/normals/ids/primvars vs the count their interpolation implies
(vertex/varying → points, faceVarying → face-vertices, uniform → faces, constant →
1), and `sum(faceVertexCounts) == len(faceVertexIndices)` with indices in range.

## Consequences

- Authoring bugs are caught automatically (used at every milestone).
- usd-core is a **dev/validation** dependency only — never imported inside TD, never
  required to produce an export.
- `tools/.venv-usd/` is gitignored; `tools/validate_usd.py` is committed.
- The same validator works on streamed and changing-topology output (USD value
  resolution is transparent to it).
