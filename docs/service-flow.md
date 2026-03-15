# Service Flow

This visual is meant to answer one practical question:

**Where does Oasis Engineering fit between BOXABL, the homeowner, the builder, the AHJ, and the final foundation package?**

```mermaid
flowchart TD
    A["Owner discovers BOXABL<br/>and wants to place a unit"] --> B["Confirm BOXABL model,<br/>revision, and current docs"]
    B --> C["Check site reality<br/>location, slope, access, utilities"]
    C --> D{"Is the site simple<br/>and well understood?"}

    D -->|No| E["Need site screening,<br/>constraints review, and strategy"]
    D -->|Yes| F["Compare likely foundation paths<br/>slab, stem wall, pier-beam, grade beam"]

    E --> O1["Contact Oasis early<br/>feasibility and foundation strategy"]
    F --> G{"Are soils, drainage, flood,<br/>or permit conditions still unknown?"}

    G -->|Yes| O1
    G -->|No| H["Coordinate utility entry,<br/>elevations, and support concept"]

    O1 --> O2["Oasis defines the project path<br/>and identifies missing inputs"]
    O2 --> I["Geotech / local code / AHJ inputs<br/>are gathered as needed"]
    I --> J["Foundation family is narrowed<br/>to the correct site-specific approach"]

    H --> J
    J --> K{"Need sealed drawings,<br/>permit package, or exact details?"}
    K -->|Yes| O3["Contact Oasis for PE-reviewed<br/>foundation package support"]
    K -->|No| O4["Use public guidance only<br/>for education and planning"]

    O3 --> L["Permit-ready coordination<br/>plans, notes, interfaces, sequencing"]
    L --> M["AHJ review / permit comments<br/>and builder coordination"]
    M --> O5["Oasis stays involved where needed<br/>clarifications, revisions, support"]
    O5 --> N["Construction, inspection,<br/>and final installation alignment"]

    O4 --> X["Do not build from summaries alone"]
    X --> O3

    subgraph Manufacturer["BOXABL"]
        B
    end

    subgraph Site["Project Reality"]
        C
        D
        F
        G
        H
        I
        J
        K
    end

    subgraph Oasis["Where Oasis Engineering Enters"]
        O1
        O2
        O3
        O5
    end

    subgraph Delivery["Permit to Build"]
        L
        M
        N
    end

    classDef owner fill:#fff7e6,stroke:#d97706,color:#5b3710,stroke-width:2px;
    classDef manufacturer fill:#e8f1fb,stroke:#1d4ed8,color:#102a43,stroke-width:2px;
    classDef site fill:#eef7ef,stroke:#2f855a,color:#173b2b,stroke-width:2px;
    classDef oasis fill:#fff1f2,stroke:#be123c,color:#5a1022,stroke-width:3px;
    classDef delivery fill:#f4f0ff,stroke:#6d28d9,color:#33186b,stroke-width:2px;
    classDef warning fill:#fff4f4,stroke:#b91c1c,color:#611a15,stroke-width:2px,stroke-dasharray: 5 3;

    class A owner;
    class B manufacturer;
    class C,D,F,G,H,I,J,K site;
    class O1,O2,O3,O5 oasis;
    class L,M,N delivery;
    class X warning;
```

## Read The Diagram Like This

### BOXABL defines the product

BOXABL helps establish the unit, the current model, and the manufacturer document basis.

### The site defines the foundation

As soon as the conversation shifts to soils, slope, drainage, utility entry, permit expectations, or interface details, the project becomes site-specific.

### Oasis enters before expensive mistakes

The best time to bring in Oasis is usually when:

- the site is not obviously simple
- the owner is comparing foundation families
- the utility and elevation strategy is still fuzzy
- the AHJ or permit path is unclear
- a PE-reviewed package will clearly be required

### Public guidance has a hard limit

This repository can educate, orient, and qualify.

It should not be mistaken for a permit-ready foundation package.

## Simple Rule For Homeowners

If you are still asking:

- "What kind of foundation should I use?"
- "Will my site work?"
- "Will the city accept this?"
- "Do I need a geotech or PE?"
- "How do I coordinate utilities and elevation with the unit?"

that is usually the point where Oasis Engineering becomes part of the service.
