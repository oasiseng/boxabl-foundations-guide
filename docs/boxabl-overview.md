# BOXABL Overview

## What BOXABL Appears to Offer

BOXABL markets factory-built housing and a staged delivery process that includes model selection, feasibility, site preparation, delivery, and setup.

Online references (verification dates in [`data/SOURCES.yaml`](../data/SOURCES.yaml)):

- [BOXABL Home](https://www.boxabl.com)
- [How It Works](https://www.boxabl.com/how-it-works)
- [Technical Documentation](https://www.boxabl.com/technical-docs)

BOXABL's public site highlights a Casita lineup plus the Baby Box, and in June 2026 BOXABL announced a "Phase 2" catalog with additional connectable and stackable models. The lineup changes — always verify the current models, revision history, and approved document set directly from BOXABL before relying on a model assumption.

## BOXABL Model Lineup

All numbers trace to [`data/models.yaml`](../data/models.yaml), which records a verification status for every fact.

| Model | Model # | Size | Config | Modules | Details |
|-------|---------|------|--------|---------|---------|
| Studio Casita | BXB-000009 (verified via install manual) | 361 sq ft | Studio / 1 bath | Single | [Studio Casita](studio-casita.md) — flagship model; ideal for ADU/guest house |
| 1-Bedroom Casita | confirm with BOXABL | ~722 sq ft | 1 bed / 1 bath | **Dual** | [1-Bedroom Casita](one-bedroom-casita.md) — two connected 19' x 19' modules |
| 2-Bedroom Casita | BXB-000016 (unverified) | ~722 sq ft | 2 bed / 1 bath | **Dual** | [2-Bedroom Casita](two-bedroom-casita.md) — dual-module with inter-module connections |
| Baby Box 120 RV | BXB-000029 | ~120 sq ft class | Studio RV | Single | [Baby Box 120 RV](baby-box-120-rv.md) — towable RV with integrated chassis; not a permanent-foundation project |

> **Correction notice (June 2026):** earlier versions of this repo assigned BXB-000009 to a 722 sq ft single-module "1-Bedroom Casita." The published BXB-000009 Installation Manual identifies that model number as the 361 sq ft Studio Casita, and BOXABL's public material describes the 1- and 2-Bedroom layouts as 19' x 38' dual-module products. Dealer material also reports the dual-module models as California-only as of late 2025 — verify with BOXABL.

## Foundation-Relevant Open Facts

All BOXABL permanent-foundation models use **ICC-ES ESR-4725 certified structural insulated panels** (SIPs).

See [ICC-ES ESR-4725 Structural Insulated Panel Certification](icc-es-esr-4725.md) for structural, thermal, and code compliance details — and note the verification caveats on that page about the current report revision and code-cycle recognition.

For the reference BXB-000009 Studio Casita, the installation manual (Rev 1.1) lists:

- unfolded dimensions: 19' L x 19' W x 10'-9" H (361 sq ft)
- shipping dimensions: 19' L x 8'-6" W x 12'-4" H
- approximate weight: 12,800 lb
- R-values: R-23.47 walls / R-28.3 floor / R-27.68 flat roof
- snow and wind loads: deferred to the structural plans for each roof type
- manufacturer direction to refer to the approved plan set for foundation designs and connections, with custom foundation designs approved by the local AHJ

Useful references:

- [BXB-000009 Installation Manual](https://gcdn.boxabl.com/documents/technical/plan-sets/BXB-000009%20Install%20Manual.pdf)
- [Casita Specifications](https://gcdn.boxabl.com/documents/technical/Casita%20Specifications%205-21-24.pdf)

A phrasing note for anyone repeating specs: a **seismic design category is a site property**, determined by location and soils. Describe units as "rated for sites up to a given SDC per manufacturer materials," never as "this unit is SDC D."

## What BOXABL Information Usually Does Not Finish for You

Even when manufacturer documentation is available, the owner still has to resolve:

- jurisdiction and permit path
- local code adoption
- site-specific soil and bearing assumptions
- foundation selection
- utility routing and utility elevations
- drainage and finished floor elevation
- site access for delivery and equipment
- local PE review, seals, and inspection requirements

## Baby Box Note

The Baby Box deserves its own intake path because the official public material describes it as a **towable recreational vehicle** with an **integrated chassis**, adjustable suspension, and leveling capability.

That means some leads may need a siting and support strategy more than a traditional permanent-foundation answer.

See [Baby Box 120 RV / BXB-000029](baby-box-120-rv.md).

## Dual-Module Note

The 1-Bedroom and 2-Bedroom Casitas are dual-module products. For those leads, inter-module connection design and unified bearing behavior are first-class engineering topics — see the model pages for the specifics.

## Practical Translation

The modular unit may be standardized.

The foundation is not.

That is the gap this repository is built to explain.

## What to Verify Before Any Design Commitment

- exact BOXABL model number and revision (do not trust older internet posts — this repo itself carried a wrong model-number mapping until June 2026)
- current official manufacturer manual and specs
- state availability for dual-module models
- whether BOXABL generic foundation information is accepted by the local AHJ
- whether a geotechnical report is required
- whether the project needs wet-sealed site-specific engineering
- exact utility stub locations and finished floor targets
