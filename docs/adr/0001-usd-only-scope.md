# ADR 0001 - USD-Only Export Scope

Status: Accepted

## Context

The project exists to export animated SOP geometry from TouchDesigner into a format
that downstream DCC tools can import as a single animated cache. The practical
validation targets are Houdini, Blender, usdview, and other USD-capable tools.

## Decision

Target **USD only**. The public positioning, UI, documentation, tools, and
architecture should describe the project as a TouchDesigner SOP-to-USD exporter.
Supported output files are `.usda` and `.usdc`.

## Consequences

- One cache format to author, validate, document, and support.
- Search/discovery copy should include TouchDesigner, SOP, geometry, animation, and
  USD terminology.
- Non-USD export work is outside this project's scope.
