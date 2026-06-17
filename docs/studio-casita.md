# Boxabl Studio Casita / BXB-000009

This page is the **model-specific public briefing** for the BOXABL Studio Casita, model `BXB-000009`.

It exists because this is BOXABL's flagship and smallest permanent-foundation model — ideal for ADU, guest house, and accessory structure classification in many jurisdictions — and because it is the only model in this repo whose core specs are verified against a published manufacturer manual.

> **Correction notice (June 2026):** Earlier versions of this repo assigned model number BXB-000009 to a 722 sq ft "1-Bedroom Casita." That was incorrect. The published BXB-000009 Installation Manual identifies this model number as the **361 sq ft Casita**. All specs below trace to [`data/models.yaml`](../data/models.yaml).

## Official Open Source Position

Official published references (verification dates in [`data/SOURCES.yaml`](../data/SOURCES.yaml)):

- [BOXABL Home](https://www.boxabl.com)
- [Technical Documentation](https://www.boxabl.com/technical-docs)
- [BXB-000009 Installation Manual](https://gcdn.boxabl.com/documents/technical/plan-sets/BXB-000009%20Install%20Manual.pdf)

The official material describes the Studio Casita as:

- single-module factory-built housing unit
- studio-style floor plan with full kitchen, full bathroom, and a defined sleeping area
- ICC-ES ESR-4725 certified structural insulated panels
- designed for permanent foundation installation

## Public Facts That Matter For Lead Intake

**Verified against the BXB-000009 Installation Manual (Rev 1.1):**

- unfolded dimensions: 19' L x 19' W x 10'-9" H (361 sq ft)
- shipping dimensions: 19' L x 8'-6" W x 12'-4" H
- approximate shipping weight: 12,800 lbs
- R-values: R-23.47 walls / R-28.3 floor / R-27.68 flat roof
- snow and wind loads: **the manual defers to the structural plans for allowable loading of each roof type** — do not quote a single universal mph or psf rating
- delivery: forklift, telehandler, or crane methods per the manual; site must support equipment plus unit weight
- foundation: the manual directs users to the approved plan set for approved generic foundation designs and connections; custom foundation designs are approved by the local AHJ

**From BOXABL's public site (unverified — confirm before relying):**

- ceiling height: approximately 9'-6"
- approximate list price: ~$60,000 (changes frequently; verify with BOXABL)
- floor live load, roof live load, and seismic ratings: see the structural plans and current spec sheet for the unit revision in question

**Certification & Code Compliance:**

- ICC-ES ESR-4725 certified SIP panels (see [ICC-ES ESR-4725](icc-es-esr-4725.md))
- report recognition listed under 2021/2018 IBC and IRC — verify the current report revision and the code cycle adopted locally before permit use

## Why This Model Deserves Its Own Foundation Path

1. **Smallest permanent-foundation footprint.** At 19' x 19' (361 sq ft), it often qualifies as an ADU, guest house, or accessory structure under local zoning.

2. **Single-module simplicity.** Unlike the 1-Bedroom and 2-Bedroom Casitas (dual-module, ~722 sq ft), there is no inter-module connection complexity. The foundation supports one unified unit.

3. **Best-documented model.** The installation manual is publicly available, which means specs can be verified instead of assumed. The manual itself states that the approved drawings control over the manual in any discrepancy — a principle this repo follows too.

4. **Easiest permitting profile.** Many jurisdictions have streamlined ADU or accessory structure approval paths. The Studio often fits those categories faster than a full residence.

5. **Most production-proven.** This is the unit BOXABL has delivered in volume, so delivery logistics, utility coordination, and permitting paths are comparatively well established.

## What "Foundation Plan" Means For The Studio Casita

### Standard Foundation Options

Studio projects typically use one of these (see [Foundation Options](foundation-options.md)):

**Concrete Slab:**
- solid bearing pad with vapor barrier and gravel base
- continuous footing perimeter or spot bearing at panel connections
- simple utility penetrations (fewer than larger models)
- typical choice for straightforward sites

**Concrete Pier & Beam:**
- engineered pier layout supporting beam lines under the unit
- useful for sloped sites or drainage sensitivity
- allows flexible utility routing and grading

**Crawlspace with Stem Wall:**
- perimeter stem wall with interior bearing
- adds elevation control and moisture management
- useful where utilities need elevation or long-term serviceability is critical

**Grade Beam:**
- continuous reinforced beam on stable bearing layer
- useful for sites requiring a unified support strategy or local code preference

### Key Coordination Items

Regardless of foundation family:

- site access for forklift/telehandler/crane delivery
- utility stub locations (water, power, waste, vent)
- finished floor elevation and slope drainage
- bearing soil capacity (geotechnical report typical)
- anchorage connection to panel base per the approved plan set
- local building official review and approval path

## What BOXABL Does vs. What You Define

**BOXABL provides:**
- structural panel specifications and ESR-4725 certification
- the installation manual and approved plan set
- shipping and placement dimensions
- installation sequencing guidance

**You (and Oasis) define:**
- site-specific foundation selection
- bearing capacity and soil assumptions
- exact anchorage connection geometry (using defined connection points)
- local permit path and code compliance
- utility routing and elevations
- final construction sequencing
- site-specific engineering seal and inspection

## Oasis Role For A Studio Casita Lead

- confirm the project fits ADU or accessory structure classification in the target jurisdiction
- select the optimal foundation family for the site and local code
- coordinate utility, grading, and finished floor elevation
- design site-specific connection and anchorage
- support permit intake and AHJ review
- provide PE-sealed drawings and inspection support
- advise on long-term site settlement and serviceability

## Public-Safe Guidance For Studio Leads

Do not assume:

- that a smaller footprint eliminates foundation engineering rigor
- that all jurisdictions accept factory-built ADU classifications without review
- that the manual's generic foundation references replace site-specific design — the manual itself says custom foundation designs are approved by the local AHJ
- that permitting will be automatically faster

Do assume:

- the manual is the starting point, not the final design, and the approved drawings control
- single-module delivery is simpler than dual-module coordination
- local classification and code acceptance must be verified early
- geotechnical and utility planning still matter

## Recommended Intake For A Studio Lead

Collect these first (store using the field names in [`data/foundation-intake.schema.json`](../data/foundation-intake.schema.json)):

- site address and jurisdiction
- intended use (primary ADU, guest house, rental, property expansion)
- whether ADU or accessory structure classification is likely
- site slope and drainage condition
- existing utility infrastructure (power, water, sewer/septic)
- lot size and setback constraints
- whether the AHJ has reviewed factory-built or modular construction before
- delivery access (forklift/telehandler/crane available)
- owner's timeline and permitting readiness

## Verification Statement

Always verify current specs directly with BOXABL before design or permit decisions. Manual-verified facts above were checked against BXB-000009 Installation Manual Rev 1.1 on the date recorded in [`data/SOURCES.yaml`](../data/SOURCES.yaml). For the latest documentation, visit [BOXABL Technical Docs](https://www.boxabl.com/technical-docs).

For foundation design and permitting, Oasis Engineering can translate these specs into a site-specific plan that fits your jurisdiction and site conditions.
