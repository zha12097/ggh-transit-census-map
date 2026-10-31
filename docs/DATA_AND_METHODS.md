# Data and methods

## Geographic coverage

The map displays 99 municipalities from a project-defined selection of the Greater Golden Horseshoe. The boundary layer was prepared by the author from Statistics Canada Census Subdivision (CSD) boundaries. The selected geography is not an official Census delineation of the GGH, and the source release year should be confirmed before citing a particular boundary-file edition.

The CSD layer was simplified for web display. A polygon self-intersection identified in **Township of Ramara** (CSD `3543019`) was repaired for this release with Shapely/GEOS `make_valid`. The resulting valid MultiPolygon was retained; a zero-area line fragment was discarded. Feature count, attributes, Census join identifiers, and area were retained within rounding precision. The original author-produced boundary layer is open for reuse with Statistics Canada attribution under the Statistics Canada Open Licence.

## Transit data

The map contains 387 transit point features and 127 route features from RTP GIS inputs supplied for the project. Each carries a technology and project-status classification. These are planning features, not real-time service feeds. Only simplified display geometries and selected feature attributes are embedded in `index.html`; original source GIS files are not published separately.

The permissions for redistributing the original RTP files have not been independently confirmed. Visitors should understand that the features embedded in the HTML page are publicly retrievable, irrespective of whether the original files are listed for download.

## Census data

Statistics Canada 2016 and 2021 Census Profiles were linked to the 99 CSDs by geographic identifiers. The map contains 57 numeric indicators for each CSD and Census year. The values are included in the HTML for client-side rendering; the original full Census downloads, filtered profile tables and intermediate processed files are not published in this repository.

Indicator panels:

- **Counts & Levels:** population, housing and dwelling measures, labour force and commuting counts.
- **Percentages & Rates:** demographic, housing, employment and commuting proportions.
- **Labour Force by Industry:** 20 industry categories for the **resident** labour force, not for jobs physically located within the municipality.

Quantile cutoffs are calculated across the 99 municipalities for the active indicator and year. Classes are relative to this project's geographic sample, not absolute thresholds for Ontario.

## Comparability

The project uses one version of municipal boundaries for both Census years. It does not implement a historical boundary-harmonization model. Some attributes represent 25% sample estimates and different reference periods; in particular, household income refers to 2015 or 2020, the 2021 commute period was affected by COVID-19, and the industry classifications reference different NAICS versions. The presence of two Census years should not be mistaken for a fully harmonized time-series dataset.

## Data access and attribution

- Statistics Canada CSD boundary datasets and this author's derived municipal selection are open, subject to appropriate source attribution and the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence).
- Original Statistics Canada Census publications remain accessible from Statistics Canada. Original published Census datasets are not made private by this repository's decision not to host extracts.
- Original RTP GIS source files are not separately hosted or offered for unrestricted redistribution. Inquiries may be directed through GitHub issues and assessed against provider conditions.
- All geometry and values sent to browsers in `index.html` are public and technically extractable. This repository does **not** enforce access controls on the embedded map data.

The main map is a descriptive exploratory tool; it should not be used as a substitute for authoritative project status, current service information or official population estimates.
