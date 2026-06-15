# ADR 0005 — Native TD Mesh tessellation; single Poly ingestion path

Status: Accepted

## Context

A USD mesh is `faceVertexCounts` + `faceVertexIndices` (tris and n-gons are the same
code; only the per-face count differs). TouchDesigner exposes several primitive
types. The reader iterates `sop.prims`, where each `Poly` prim is one face. A TD
`Mesh`-type primitive is instead a single rows×cols grid prim — reading it naively
yields one giant n-gon.

## Decision

Support both `Poly` and the TD `Mesh` primitive natively:

- `Poly` prims pass through as one face each.
- `Mesh` prims are tessellated from their grid (`numRows`/`numCols`, honoring
  `closedU`/`closedV` wrap) into quads. Degenerate pole rings (a collapsed grid row
  at a sphere pole) are de-duplicated into triangles; fully degenerate cells are
  dropped. Verified to match a TD Convert SOP exactly (e.g. a sphere → 760 faces =
  80 pole triangles + 680 quads).
- Prim attributes are replicated per **output** face (a Mesh prim emits many faces),
  keeping `uniform` interpolation counts correct.
- Other prim types (NURBS, Bezier, …) raise with a "Convert to Polygon" hint.

## Consequences

- The exporter handles more than TD's per-face primitive out of the box; no upstream
  Convert SOP needed for Poly or Mesh.
- Curves/NURBS remain a separate, larger effort (different USD schemas).
- Mixed `Poly` + `Mesh` prims merge into one `UsdGeomMesh` correctly. Mixing loose
  points with faces makes the points unreferenced vertices (use distinct geometry,
  not a merge — multi-prim output is not supported).
