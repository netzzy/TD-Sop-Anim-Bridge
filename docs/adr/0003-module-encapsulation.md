# ADR 0003 — Encapsulate in one Base COMP with a Python extension

Status: Accepted

## Context

The exporter must drop cleanly into real projects and survive copy/`.tox` export.
TouchDesigner's idiomatic unit of reuse is a self-contained COMP.

## Decision

The whole module lives in a single Base COMP, `TD_SOP_USD_Anim_Bridge`:

- Input geometry arrives through the COMP's input connector and is read from the
  inner `IN_FOR_EXPORT` (In SOP). Nothing outside the COMP is referenced.
- All logic is a promoted Python **extension** (`ExportExt` Text DAT, referenced by
  `par.extension1`), driven by calling methods on the COMP (e.g. `comp.Export()`).
- All UI is **custom parameters** on the COMP — no panel building.
- A `parexec_export` parameterexecute DAT dispatches the `Export` pulse to the
  extension (extension pulse callbacks do not fire on their own).
- References inside the module are relative (`op('IN_FOR_EXPORT')`, `me.time`), never
  hardcoded `/project1/...`.

## Consequences

- Copy-/`.tox`-safe and portable.
- Persisting work means saving the `.toe` (the extension lives in the binary). The
  project-save discipline (save before/after risky changes) follows from this.
