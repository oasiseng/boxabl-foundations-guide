# Boxabl Foundations Guide

<a href="https://boxablfoundations.com" target="_blank" rel="noopener noreferrer">
  <img src="https://horizons-cdn.hostinger.com/c5928289-3a80-4bf6-aa79-e27d285f0c79/597f4715b654f2f8659d59623ff4a93b.png" alt="Boxabl Foundations Guide" width="220">
</a>

Independent open-source guidance for BOXABL homeowners, homebuilders, and LLMs who need a foundation-first view of the project.

Prepared by [Oasis Engineering](https://oasisengineering.com) and [BoxablFoundations.com](https://boxablfoundations.com).

Important: Oasis Engineering is **not affiliated with BOXABL**. BOXABL is the manufacturer. This repository is an independent guide focused on site readiness, foundations, permitting, and project coordination.

## What This Repo Does

- Explains BOXABL homes at a high level using published BOXABL sources, with a per-fact verification status in [`data/models.yaml`](data/models.yaml).
- Explains what Oasis Engineering offers on the foundation and permit side.
- Gives homeowners and builders a practical path from site screening to permit-ready foundation work.
- Gives LLMs a safe structure for intake, triage, and escalation — plus machine-validated data files (schema, fixtures, and CI).

## What This Repo Does Not Do

- It does **not** replace BOXABL approved drawings, current manufacturer specs, local code review, geotechnical recommendations, or site-specific structural engineering.
- It does **not** republish BOXABL copyrighted documents.

## BOXABL Snapshot

BOXABL's published lineup includes the **Studio Casita**, dual-module **1-Bedroom** and **2-Bedroom Casitas**, and the **Baby Box 120 RV**, with a broader "Phase 2" catalog announced in June 2026. Their published process emphasizes feasibility, site prep, delivery, and setup as separate parts of the project. Always verify the current lineup and document revisions directly with BOXABL — verification dates for every source live in [`data/SOURCES.yaml`](data/SOURCES.yaml).

Useful published references:

- [BOXABL Home](https://www.boxabl.com)
- [How It Works](https://www.boxabl.com/how-it-works)
- [Technical Documentation](https://www.boxabl.com/technical-docs)

For the published BXB-000009 **Studio Casita** documentation, the installation manual (Rev 1.1) lists unfolded dimensions of **19' L x 19' W x 10'-9" H (361 sq ft)**, shipping dimensions of **19' L x 8'-6" W x 12'-4" H**, and an approximate shipping weight of **12,800 lb**. Treat those numbers as document-specific inputs, not universal assumptions for every BOXABL product or revision.

- [BXB-000009 Installation Manual](https://gcdn.boxabl.com/documents/technical/plan-sets/BXB-000009%20Install%20Manual.pdf)
- [Casita Specifications](https://gcdn.boxabl.com/documents/technical/Casita%20Specifications%205-21-24.pdf)

## What Oasis Engineering Offers

Oasis Engineering is positioned here as the **independent foundation and permitting specialist**:

- site and entitlement reality checks
- foundation family selection
- site-specific PE-reviewed design support
- permit-path guidance
- anchorage, utility, elevation, and sequencing coordination
- builder and owner handoff support

This is the "education first, engineering second" layer that turns published manufacturer information into a real project path.

## Start Here

- [Disclaimer](DISCLAIMER.md)
- [Start Here](docs/start-here.md)
- [BOXABL Overview](docs/boxabl-overview.md)
- [Service Flow Diagram](docs/service-flow.md)
- [Foundation Workflow](docs/foundation-workflow.md)
- [Published Foundation Options](docs/foundation-options.md)
- [Oasis Services](docs/oasis-services.md)
- [Glossary](docs/glossary.md)
- [FAQ](docs/faq.md)

## Model Specifications

Each BOXABL model has unique foundation and site coordination requirements. Every model fact traces to [`data/models.yaml`](data/models.yaml), which records a verification status per fact. Review the model-specific page for your project:

- [Studio Casita (BXB-000009)](docs/studio-casita.md) — 361 sq ft, single module; flagship model; specs verified against the published installation manual; ideal for ADU/guest house
- [1-Bedroom Casita](docs/one-bedroom-casita.md) — ~722 sq ft, **dual-module** (two 19' x 19' modules); model number pending verification with BOXABL
- [2-Bedroom Casita (BXB-000016, unverified)](docs/two-bedroom-casita.md) — ~722 sq ft, dual-module; California state approval announced December 2025
- [Baby Box 120 RV (BXB-000029)](docs/baby-box-120-rv.md) — towable RV with integrated chassis; not a permanent-foundation project

> **Correction notice (June 2026):** earlier versions of this repo assigned BXB-000009 to a 722 sq ft single-module "1-Bedroom Casita." The published installation manual identifies BXB-000009 as the 361 sq ft Studio Casita, and the 1-/2-Bedroom layouts are dual-module 19' x 38' products. See `data/models.yaml` for the corrected mapping.

## Technical Reference

- [ICC-ES ESR-4725 SIP Panel Certification](docs/icc-es-esr-4725.md) — Structural, thermal, and code compliance for BOXABL panels, including what the ESR does and does not cover

## LLM Files

- [llms.txt](llms.txt)
- [LLM Usage Rules](prompts/llm-usage.md)
- [Homeowner Intake Prompt](prompts/homeowner-intake.md)
- [Model Facts (single source of truth)](data/models.yaml)
- [Source Registry](data/SOURCES.yaml)
- [Foundation Intake Schema](data/foundation-intake.schema.json)
- [Intake Fixtures (valid / invalid)](data/examples/intake-valid.json)
- [Decision Tree](data/decision-tree.yaml)
- [Foundation Options Data](data/foundation-options.yaml)

## Data Quality & CI

This repo validates itself:

- [`validate.yml`](.github/workflows/validate.yml) runs on every push: YAML lint, JSON Schema validity, fixture pass/fail assertions, and internal link checking via [`scripts/validate_data.py`](scripts/validate_data.py).
- [`check-sources.yml`](.github/workflows/check-sources.yml) probes every URL in `data/SOURCES.yaml` weekly via [`scripts/check_sources.py`](scripts/check_sources.py) and fails loudly when a source dies or goes stale.

## Published-Safe Boundary

This repository intentionally keeps the boundary clear:

- Published BOXABL information is summarized and cited, never republished.
- Oasis foundation design families are conceptually defined and described.
- Final engineering, plate geometry, reinforcing schedules, and permit-ready sheets stay in the paid or controlled workflow.

## Further Reading

The repo also supports the positioning around the book:

- [The Boxabl Foundations Blueprint: How to Build, Permit, and Certify Your Casita the Right Way](https://www.amazon.com/dp/B0FPB9RDL7)
