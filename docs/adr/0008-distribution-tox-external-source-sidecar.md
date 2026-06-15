# ADR 0008 - Distribution via `.tox`, external source, and reproducible sidecar

Status: Accepted

## Context

The exporter worked in the development `.toe`, but a cloned repository was not yet
ready for other users. The Python extension lived only inside the binary project,
binary `.usdc` export depended on a machine-local `tools/.venv-usd`, and there was
no committed drop-in component or setup recipe.

## Decision

Ship the module in three coordinated forms:

- `TD_SOP_USD_Anim_Bridge.tox` as the reusable drop-in component.
- `src/ExportExt.py` as the canonical, reviewable extension source, synced to the
  component's `ExportExt` DAT.
- `tools/setup.py` plus `tools/requirements.txt` to rebuild the optional usd-core
  sidecar used for `.usdc` transcode and validation.

The component adds `USD Python`, `Setup Binary Support`, and `Binary Status` custom
parameters. `.usdc` transcode resolves Python in this order: explicit `USD Python`
parameter, `TD_SOP_USD_ANIM_BRIDGE_PYTHON`, then `tools/.venv-usd`. The setup pulse runs
`tools/setup.py` with TouchDesigner's bundled Python and reports status in the
textport and `Binary Status`.

## Consequences

- `.usda` export remains zero-setup for TouchDesigner users.
- `.usdc` export is one reproducible setup step away and no longer hardcodes a
  Windows-only interpreter path.
- Code review can happen against `src/ExportExt.py` instead of a binary `.toe`.
- Maintaining behavior now requires keeping the `.py`, DAT, `.toe`, and `.tox` in
  sync when exporter code changes.
