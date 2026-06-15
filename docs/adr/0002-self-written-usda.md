# ADR 0002 — Write `.usda` ourselves; usd-core only validates

Status: Accepted

## Context

TouchDesigner has **no native USD writer** (the USD COMP imports only). TD's Python
(3.11) does **not** expose the `pxr`
bindings — the internal USD is C++ only. So we must author the file ourselves.

Installing `usd-core` into TD's own Python is risky: the TD process already loads
its own USD + TBB DLLs, so a second USD runtime in-process can clash.

## Decision

Author **`.usda` (ASCII USD)** directly from the extension using only the Python
standard library. ASCII is human-readable (eyeball-verifiable on small exports) and
needs no third-party library inside TD. Use `usd-core` **only out-of-process for
validation** (see [0006](0006-usd-core-validation-venv.md)).

## Consequences

- No dependency or DLL-clash risk inside TouchDesigner.
- `.usdc` is not authored directly in TD. ADR
  [0007](0007-binary-usdc-via-transcode.md) adds it as an out-of-process sidecar
  transcode from the `.usda` writer, with the expected whole-layer RAM cost in the
  sidecar.
- We own the USD serialization details (interpolation, time samples, topology).
