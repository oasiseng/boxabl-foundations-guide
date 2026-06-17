# Boxabl 1-Bedroom Casita (Dual-Module, 722 sq ft)

This page is the **model-specific public briefing** for the BOXABL 1-Bedroom Casita.

> **Correction notice (June 2026):** Earlier versions of this page assigned model number `BXB-000009` to the 1-Bedroom Casita and described it as a single module. Both claims were wrong. Per the published installation manual, **BXB-000009 is the 361 sq ft Studio Casita** — see [Studio Casita](studio-casita.md). BOXABL's public material describes the 1-Bedroom layout as **19' x 38' at 722 sq ft**, which is **two connected 19' x 19' modules**. The correct 1-Bedroom model number has not yet been verified — confirm it directly with BOXABL and record it in [`data/models.yaml`](../data/models.yaml).

## Official Open Source Position

Official published references (verification dates in [`data/SOURCES.yaml`](../data/SOURCES.yaml)):

- [BOXABL Home](https://www.boxabl.com)
- [Technical Documentation](https://www.boxabl.com/technical-docs)

BOXABL's public material describes the 1-Bedroom Casita as:

- a one-bedroom, one-bath layout at approximately 722 sq ft
- approximately 19' x 38' unfolded — i.e., **two connected 19' x 19' modules**
- full kitchen with full-size appliances, built-in closets, 9'-6" ceilings
- ICC-ES ESR-4725 certified structural insulated panels
- designed for permanent foundation installation

**Availability caveat:** as of late 2025, dealer material reported the 1-Bedroom and 2-Bedroom models as offered **only in California**. Confirm current availability and approved states directly with BOXABL before qualifying a lead outside California.

## Public Facts That Matter For Lead Intake

All items below are **unverified against a primary manual** for this specific model — treat them as intake starting points, not design inputs:

**Dimensions & Configuration:**
- unfolded footprint: approximately 19' x 38' (~722 sq ft)
- configuration: 1 bedroom / 1 bath, full kitchen
- modules: two 19' x 19' modules connected on-site
- per-module shipping expected to be similar to the Studio (19' L x 8'-6" W x 12'-4" H) — confirm with BOXABL
- delivery: two transport/unfolding sequences plus inter-module connection work

**Structural & Building Science:**
- SIP panel construction certified under ICC-ES ESR-4725 (see [ICC-ES ESR-4725](icc-es-esr-4725.md))
- wall/floor/roof R-values expected to match the published panel family (R-23.47 / R-28.3 / R-27.68) — confirm for this model's revision
- snow, wind, and seismic ratings: see the structural plans for the unit revision; do not quote universal numbers

**Pricing & Availability:**
- pricing for the dual-module models changes frequently and varies by state — verify with BOXABL before quoting anything

## Why The 1-Bedroom Requires Dual-Module Thinking

Because this is a two-module product, the foundation logic is closer to the [2-Bedroom Casita](two-bedroom-casita.md) than to the single-module Studio:

1. **Inter-module connection engineering.** The two modules must be joined at a defined interface, coordinated with the foundation, and verified during installation.

2. **Unified bearing surface.** The foundation cannot be two independent 19' x 19' pads with uncoordinated settlement behavior. Differential settlement at the module seam is the failure mode to design against.

3. **Larger footprint, more utility coordination.** Stubs and penetrations span both modules; routing must be planned across the full ~19' x 38' footprint.

4. **Two delivery sequences.** Two crane/telehandler events, two unfolding operations, tighter site logistics.

## What "Foundation Plan" Means For The 1-Bedroom Casita

The realistic options mirror the dual-module strategies described in detail on the [2-Bedroom Casita](two-bedroom-casita.md) page:

- **unified concrete slab** across the full dual-module footprint (most common)
- **pier & beam with a dual-module layout**, including support at the module interface
- **crawlspace with stem wall** spanning both modules
- **grade beam** providing continuous support lines under both modules

In every case, the inter-module interface and unified settlement behavior drive the design — not just the perimeter loads.

## Oasis Role For A 1-Bedroom Casita Lead

- confirm the correct model number and current documentation with BOXABL before anything else
- verify availability for the lead's state
- review the inter-module connection specification and coordinate it with the foundation design
- select a unified foundation family for the site and local code
- coordinate utility, grading, and finished floor elevation across both modules
- provide PE-sealed drawings, inspection support, and AHJ response

## Public-Safe Guidance For 1-Bedroom Leads

Do not assume:

- that single-module (Studio) foundation logic applies
- that the model number from older internet posts is current — verify it
- that the product is available in the lead's state without checking
- that two separate pads are acceptable

Do assume:

- the panel technology and certification match the rest of the Casita family
- inter-module connection and unified bearing are explicitly engineered items
- a geotechnical report is strongly advisable for dual-module units
- local soil, drainage, and code requirements drive final decisions

## Recommended Intake For A 1-Bedroom Casita Lead

Collect these first (store using the field names in [`data/foundation-intake.schema.json`](../data/foundation-intake.schema.json)):

- site address and jurisdiction (and whether the state is currently served by BOXABL for this model)
- exact model number and document revision from BOXABL
- intended use (primary residence, ADU, rental)
- site slope and drainage condition
- existing utility infrastructure and capacity
- lot size and setback constraints
- delivery access for two module placements
- whether the AHJ has reviewed multi-module factory-built construction before
- whether a geotechnical report is available or required

## Verification Statement

Always verify current specs, the model number, and availability directly with BOXABL before design or permit decisions. Source verification dates live in [`data/SOURCES.yaml`](../data/SOURCES.yaml). For the latest documentation, visit [BOXABL Technical Docs](https://www.boxabl.com/technical-docs).

For dual-module foundation design and permitting, Oasis Engineering can translate the manufacturer's specs into a unified site-specific plan.
