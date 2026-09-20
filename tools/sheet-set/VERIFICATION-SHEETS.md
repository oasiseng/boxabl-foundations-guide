# Sheet-set verification checklist

Complete before changing `status` from `draft`. Initial each line. A set stays PRELIMINARY until every line is initialed by the engineer of record.

## A. Data
- [ ] Every value in the project JSON traces to a source: calculation report (footing, slab, concrete), ASCE 7 Hazard Tool (wind, snow, seismic), FEMA FIRM (flood), CAL FIRE FHSZ viewer or AHJ (fire), soils report or CBC Table 1806.2 (bearing, friction), county (frost).
- [ ] `engineered: true` only if the calculation the values came from is itself verified and the values were transcribed digit-for-digit.
- [ ] Unit dimensions, plate locations and anchorage confirmed against the manufacturer's current installation drawings for the unit serial number.

## B. Sheet integrity
- [ ] `print.py` reports **no overflow** and **no JS errors** with the project loaded.
- [ ] 1-inch check square measures 1.00 in on the full-size print; 0.50 in at half size.
- [ ] Every callout on the plan resolves to a detail on the same sheet with the right number.
- [ ] Field stub, corner detail, sequence strip and takeoff show the same numbers as the calculation (spot-check four).
- [ ] Notes: masonry / wood / demolition / pier notes absent for a slab set; jurisdiction-specific items (811, special inspection, geotech trigger) match the state.

## C. Content that changes liability
- [ ] Means-and-methods / estimate disclaimer present on S1.0 and in the general notes.
- [ ] Instruments-of-service and non-affiliation notice present in the title block.
- [ ] Manufacturer images credited; no manufacturer document reproduced.
- [ ] Site plan by others stated; foundation dimensioned to its own 0,0 corner, not to property lines.
- [ ] Flood zone is not an SFHA (or the design was re-done for it).

## D. Sign-off
Engineer of record: ______________________ License: __________ Date: __________
Template version: ________ Project JSON hash / filename: ______________________
