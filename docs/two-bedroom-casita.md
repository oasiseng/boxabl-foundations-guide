# Boxabl 2-Bedroom Casita (Dual-Module, 722 sq ft)

This page is the **model-specific public briefing** for the BOXABL 2-Bedroom Casita, model number reported as `BXB-000016` (**unverified** — confirm with BOXABL and record in [`data/models.yaml`](../data/models.yaml)).

It exists because this model uses **two modules** that must be structurally connected on-site, which creates distinct foundation and coordination complexity compared to the single-module Studio.

## Official Open Source Position

Official published references (verification dates in [`data/SOURCES.yaml`](../data/SOURCES.yaml)):

- [BOXABL Home](https://www.boxabl.com)
- [Technical Documentation](https://www.boxabl.com/technical-docs)

The public material describes the 2-Bedroom Casita as:

- a dual-module factory-built housing unit (two 19' x 19' modules)
- two bedrooms, one full bathroom, complete kitchen, built-in closets
- approximately 722 sq ft (about 19' x 38' unfolded), 9'-6" ceilings
- ICC-ES ESR-4725 certified structural insulated panels
- designed for permanent foundation installation with inter-module connections

**Regulatory milestone:** BOXABL announced in December 2025 that the 722 sq ft 2-Bedroom Casita was approved under California state building laws. That approval is a strong signal for California leads, but it does not transfer automatically to other states or local AHJs.

**Availability caveat:** as of late 2025, dealer material reported the 1-Bedroom and 2-Bedroom models as offered **only in California**. Confirm current availability with BOXABL before qualifying a lead outside California.

## Public Facts That Matter For Lead Intake

All items below are **unverified against a primary manual** for this model — treat them as intake starting points, not design inputs:

**Dimensions & Configuration:**
- unfolded footprint: two modules, approximately 19' x 38' combined (~722 sq ft)
- configuration: 2 bed / 1 bath, full kitchen, laundry
- per-module shipping expected to be similar to the Studio (19' L x 8'-6" W x 12'-4" H) — confirm with BOXABL
- per-module weight: confirm with BOXABL (the Studio module is ~12,800 lbs per its manual; do not assume this transfers)
- delivery: two transport/unfolding sequences plus inter-module connection equipment

**Structural & Building Science:**
- SIP panel construction certified under ICC-ES ESR-4725 (see [ICC-ES ESR-4725](icc-es-esr-4725.md))
- wall/floor/roof R-values expected to match the published panel family (R-23.47 / R-28.3 / R-27.68) — confirm for this model's revision
- snow, wind, and seismic ratings: see the structural plans for the unit revision in question. Note that a seismic design category is a **site** property determined by location and soils — describe units as "rated for sites up to SDC D per manufacturer materials (verify)," never as "this unit is SDC D."
- each module carries panel-level certification; the inter-module connection is engineered and verified site-side

**Pricing & Availability:**
- pricing changes frequently and varies by state — verify with BOXABL before quoting

## Why The 2-Bedroom Casita Requires Its Own Foundation Path

1. **Dual-module complexity.** The unit arrives as two separate modules that must be positioned, connected structurally, and electrically unified on-site.

2. **Inter-module connection engineering.** The two modules are joined at a defined interface with structural hardware. This connection must be coordinated with the foundation and verified during installation.

3. **Larger footprint and bearing area.** The combined ~19' x 38' footprint requires more extensive foundation preparation and a larger uniform bearing area.

4. **More complex utility coordination.** Utility penetrations are split between modules, and inter-module connections must be coordinated with site utilities.

5. **Delivery logistics constraint.** Two modules mean two crane or telehandler events, two unfolding sequences, and tighter coordination on site access.

6. **The foundation must support the inter-module connection.** It cannot be two independent 19' x 19' pads with uncoordinated settlement behavior. Differential settlement at the module seam is the failure mode to design against.

## What "Foundation Plan" Means For The 2-Bedroom Casita

### Multi-Module Foundation Strategy

**Unified Concrete Slab:**
- single slab covering the entire dual-module footprint
- vapor barrier and gravel base beneath the full footprint
- continuous perimeter footing, with bearing attention under the inter-module interface
- utility penetrations pre-planned for both modules and the interface
- most common approach; simplifies bearing and leveling

**Dual-Slab with Unified Bearing:**
- separate slabs with unified base preparation
- less common; can create settlement differential and leveling challenges
- only acceptable if the inter-module interface is explicitly designed for slight movement
- requires a clear separation strategy and inspection protocol

**Pier & Beam (Dual Layout):**
- engineered pier layout supporting both modules
- piers positioned for each module's corner and center loads, plus the interface
- useful for sloped sites or drainage sensitivity

**Crawlspace with Stem Wall:**
- perimeter stem wall and interior bearing under both modules
- allows elevation control and utility access
- the inter-module connection must cross the crawlspace cleanly

**Grade Beam (Dual-Module):**
- continuous reinforced beam supporting both modules
- useful where local code or the engineer favors continuous support lines

### Key Coordination Items for Dual-Module Setup

- site access for two delivery/unfolding sequences
- utility stub locations in each module (water, sewer, electrical, vent)
- inter-module connection point and hardware location, aligned with the foundation
- finished floor elevation and slope drainage, consistent between modules
- bearing soil capacity under the entire footprint (geotechnical report strongly recommended)
- anchorage connection points in each module, sized for inter-module forces
- inter-module electrical and plumbing connections
- local building official review of inter-module connection details

## What BOXABL Does vs. What You Define

**BOXABL provides:**
- structural panel specifications and ESR-4725 certification
- floor plans for both modules and utility stub locations
- inter-module connection specification (hardware, sequence, torque)
- shipping and placement dimensions
- installation sequencing guidance

**You (and Oasis) define:**
- site-specific unified foundation design covering both modules
- bearing capacity and soil assumptions
- exact anchorage connection geometry in each module
- inter-module connection verification plan
- local permit path and code compliance
- unified utility routing and elevations
- final construction sequencing for two-module assembly
- PE-sealed drawings and inspection support

## Oasis Role For A 2-Bedroom Casita Lead

- confirm the model number, current documentation, and state availability with BOXABL
- review the inter-module connection specification and coordinate with foundation design
- select the optimal unified foundation family for the site and local code
- design a foundation that supports both modules and their connection
- coordinate utility, grading, and finished floor elevation across both modules
- establish the inter-module connection verification and inspection protocol
- support permit intake with dual-module complexity clearly explained
- provide PE-sealed drawings and inspection support

## Public-Safe Guidance For 2-Bedroom Leads

Do not assume:

- that single-module foundation logic applies to dual-module units
- that two separate 19' x 19' foundation pads are acceptable
- that the inter-module connection is self-evident from factory assembly
- that the California approval transfers to other states or local AHJs
- that standard ADU or small-structure rules apply to a dual-module unit

Do assume:

- the panel technology and certification match the rest of the Casita family
- the inter-module connection must be explicitly engineered and verified
- unified bearing and leveling are critical to long-term performance
- a geotechnical investigation is strongly recommended
- local soil, drainage, and code requirements drive final decisions

## Recommended Intake For A 2-Bedroom Casita Lead

Collect these first (store using the field names in [`data/foundation-intake.schema.json`](../data/foundation-intake.schema.json)):

- site address and jurisdiction (and whether the state is currently served by BOXABL for this model)
- exact model number and document revision from BOXABL
- intended use (primary residence, multi-family, rental)
- site slope and drainage condition
- existing utility infrastructure and capacity
- lot size and setback constraints
- whether the AHJ has reviewed multi-module factory-built construction before
- delivery access for two separate module placements
- owner's timeline and permitting readiness
- whether a geotechnical report is available or required
- any concerns about inter-module connection or settlement durability

## Verification Statement

Always verify current specs, the model number, inter-module connection details, and availability directly with BOXABL before design or permit decisions. Source verification dates live in [`data/SOURCES.yaml`](../data/SOURCES.yaml). For the latest documentation, visit [BOXABL Technical Docs](https://www.boxabl.com/technical-docs).

For foundation design, inter-module coordination, and permitting, Oasis Engineering can translate these specs into a unified site-specific plan that addresses the dual-module complexity.
