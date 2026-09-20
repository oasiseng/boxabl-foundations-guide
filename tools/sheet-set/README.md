# Foundation Sheet Set — ephemeral-eng template

Two 24×36 construction sheets rendered from one project object, in a single HTML file. Print → PDF.

- **S0.0 — the office sheet.** What you are building, design criteria, code summary, location (flood zone, fire hazard severity zone, sprinklers), HCD unit-certification note, general notes ordered by construction sequence, site images, project information.
- **S1.0 — the field sheet.** A field stub of the eight numbers a crew asks for, the foundation plan with every detail placed where it occurs, a seven-step build sequence with inspection hold points, a materials takeoff, and a means-and-methods disclaimer. Designed to be the only sheet needed on site.

The sheet design follows one rule: **drawings are for builders**. Details live next to the plan, not on another page; notes are in the order the work happens; callouts resolve on the same sheet.

## Published-safe boundary

This template ships with `PROJECT.engineered = false`. In that mode every controlled value — turndown geometry, reinforcing sizes and spacing, concrete strength, slab reinforcement, lap lengths, the materials takeoff — prints as **“per engineered design”**, and the detail slots are empty with an upload prompt. That is deliberate and matches [`data/foundation-options.yaml`](../../data/foundation-options.yaml) (`do_not_publish`).

A **controlled project JSON** (`engineered: true`, with values and detail images) turns the same file into a permit-ready set. Those files are produced in the paid workflow and are never committed here.

Nothing this template prints is a design until it is reviewed, verified per [VERIFICATION-SHEETS.md](VERIFICATION-SHEETS.md) and sealed by the licensed engineer of record.

## Use

1. `python build.py` — embeds any images found in `library/` into `dist/sheet-set.html` (only `logo.png` ships; everything else is uploaded from the panel or carried in a project JSON).
2. Open `dist/sheet-set.html`. Edit the panel or **Load project** (JSON). Every image slot has a Replace button; images are saved into the project JSON.
3. **Print / Save PDF** at 36×24, or headless: `python print.py path/to/project.json out.pdf` (Playwright + Chromium). The script also reports layout overflow, which must be empty before issuing.
4. Half size: print the PDF at 50% on 18×12 or 11×17; the title block says FULL SIZE 24×36 and carries a 1-inch check square.

## Files

| File | Purpose |
|---|---|
| `sheet-set.html` | The template. Slots 1–5 of the ephemeral-eng pattern: brand tokens, `PROJECT`, notes data, parametric SVG (isometric, corner detail), sheet pages |
| `build.py` / `print.py` | Embed library images; headless print with overflow audit |
| `library/` | Images embedded at build time (`logo.png`; optional `render.jpg`, `qr.png`, `aerial.png`, `parcel.png`, `plan.png`, `turndown.png`, `slab.png`, `plates.png`, `rebar.png`) |
| `project.schema.json` | JSON Schema for the project object (published-safe and controlled) |
| `examples/project.example.json` | A published-safe example (no engineered values) |
| `VERIFICATION-SHEETS.md` | The checklist the engineer of record completes before the PRELIMINARY band comes off |

## What the template generates from data

- General notes assemble from a tagged, sequence-ordered list; site-hazard notes (flood, FHSZ, sprinklers, HCD factory-built housing) read the project fields and rewrite themselves.
- The isometric on the cover is drawn from L × B × H when no manufacturer image is supplied.
- The corner-reinforcing detail, field stub, build sequence and materials takeoff read the same footing values the calculation used — the drawing cannot disagree with the calc.
- Callout bubbles are data; renumbering a detail is one line.
- `status` drives the PRELIMINARY / RELEASED FOR REVIEW / PERMIT / CONSTRUCTION band and watermark.

## Credit

Built on [ephemeral-eng](https://github.com/oasiseng/ephemeral-eng) by Oasis Engineering. Code under the repository MIT license; sheet design, notes and documentation under CC BY 4.0 — attribution is a condition of reuse. A one-line credit stays in the title block by default; please keep it. Cite via the repository's `CITATION.cff` where one exists.

BOXABL is a trademark of Boxabl Inc. This template and Oasis Engineering are not affiliated with, endorsed by, or sponsored by Boxabl Inc.
