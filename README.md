# Greater Golden Horseshoe: Transit and Census Map

[Open the interactive map](https://zha12097.github.io/ggh-transit-census-map/)

This project brings regional transit planning data and municipality-level Census characteristics into a single interactive map of Ontario's Greater Golden Horseshoe (GGH). It was developed to support exploratory comparison of planned transit infrastructure with local population, housing, commuting, and labour-force characteristics.

The map is a descriptive reference. It does not represent real-time transit operations or a longitudinal Census dataset harmonized to historical municipal boundaries.

## Map contents

The transit inventory contains 387 points and 127 route features from the Regional Transportation Plan (RTP) GIS inputs. Features can be filtered by project status and technology. Both filter groups offer **All** and **None** controls; technology selections for point and line layers are independent.

Municipal boundaries cover 99 Census Subdivisions (CSDs) selected for this GGH map. Boundaries can be turned on or off. A separate switch controls municipality names. The **Municipal fill opacity** slider runs from 0% (transparent) to 100% (fully opaque); the boundary outlines remain at 100% opacity. At 100%, polygons hide the OpenStreetMap basemap *inside* municipality boundaries. The OpenStreetMap basemap can also be switched off independently.

The Census interface provides **57 indicators in each of 2016 and 2021**, grouped into counts and levels, percentages and rates, and resident labour force by industry. Selecting an indicator shades the municipalities using five quantile classes calculated for the selected year. Clicking a municipality displays the Census values and geographic identifiers. Census selections are independent of the transit filters.

## Data sources

| Component | Source and treatment |
| --- | --- |
| Transit stops and routes | RTP GIS inputs supplied for this project; simplified for display |
| GGH municipal boundaries | Author-created GGH selection from Statistics Canada Census Subdivision (CSD) boundaries; simplified for web display |
| 2016 attributes | Statistics Canada, *2016 Census Profile*, 98-401-X2016066 |
| 2021 attributes | Statistics Canada, *2021 Census Profile*, 98-401-X2021021 |
| Basemap | © OpenStreetMap contributors |

### GGH municipal boundary layer

The GGH municipal boundary layer was prepared for this project from Statistics Canada's publicly available CSD boundary data. The selection covers 99 municipalities and is a project-specific geographic definition; it should not be interpreted as an official Statistics Canada GGH delineation.

**The source CSD boundaries and the author-derived GGH boundary layer are open for reuse and redistribution**, with appropriate attribution to Statistics Canada and to this project for the municipal selection and processing. The source data are covered by the [Statistics Canada Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence). The exact release year of the CSD boundary file used for this particular project remains to be confirmed; no specific source year is asserted here.

The simplified boundary geometry is included within the public HTML map. A standalone boundary download is not included in this repository. A small polygon-topology defect affecting Ramara was corrected in this release by retaining the valid polygon geometry and excluding a zero-area line remnant introduced by simplification.

### Data availability

The original RTP GIS source files, project-specific Census extracts, and intermediate processing datasets **are not deposited or separately distributed** through this repository. Questions about source files can be submitted as a GitHub issue. Requests are considered individually and do not imply permission or a commitment to share data; any release depends on the rights and conditions of the original providers.

The underlying 2016 and 2021 Census publications remain publicly available from Statistics Canada under its own licence. This project's distribution choices do not limit access to those publications.

**Information included in the map itself is public.** The single HTML page embeds simplified municipal and transit geometries and selected Census values in order to display them. A website visitor can inspect or extract those values; the absence of separately downloadable data files does not make the embedded content confidential.

## Running and maintaining the map

Open the [website](https://zha12097.github.io/ggh-transit-census-map/) using a modern browser. No installation is needed. The standalone `index.html` is the GitHub Pages entry point. Leaflet and OpenStreetMap tiles are loaded over the internet, so an internet connection is required to view the basemap.

For local testing, serve the repository over HTTP, for example with `python -m http.server 8000`, and visit `http://localhost:8000`. Avoid relying on `file://` for tile-service testing.

To publish this repository on GitHub Pages, configure **Settings → Pages → Deploy from a branch → main / (root)**. To update the website, replace `index.html` and commit the change. Additional details and test commands are provided in [`docs/MAINTENANCE.md`](docs/MAINTENANCE.md).

## Interpretation and limitations

The 2016 and 2021 observations are mapped to the same project-derived municipal boundaries, not to independently reconstructed historic CSD geometries. Comparisons across years therefore require care where municipal definitions or statistical methods differ. Income reference years are 2015 and 2020, and commuting patterns in the 2021 Census were affected by the COVID-19 pandemic. Some characteristics are based on the 25% sample.

The industry measures describe the resident labour force classified by industry. **They are not counts of jobs or workplaces located within the municipality.** The source Census years also use different NAICS reference versions (2012 and 2017). Interpret differences between industry counts accordingly.

The map uses a simplified geometry for interactive performance, and the transit inventory represents a planning dataset rather than a live schedule or inventory of completed service. This interface is for descriptive exploration, not causal inference or operational service decisions. The external Leaflet library and OpenStreetMap tile service are subject to availability and service policy.

## Repository contents

```text
index.html                 Static interactive map and embedded public display data
README.md                  Project description
.gitignore                 Local Git exclusions (not a privacy mechanism)
.nojekyll                  GitHub Pages Jekyll bypass
docs/DATA_AND_METHODS.md   Data provenance, definitions and limitations
docs/MAINTENANCE.md        Deployment and checking instructions
tests/check_map.py         Static validation of embedded data and geometry
tests/test_interactions.py Optional mocked-Leaflet browser smoke test
tests/leaflet_stub.js      Minimal Leaflet test double
.github/workflows/check.yml  Static checks on each push
```

The repository does not include a `data/` directory or the original source files. The included tests operate on the publicly embedded contents of `index.html`.

## Attribution

**Municipal boundaries:** Adapted by the project author from Statistics Canada Census Subdivision boundary data. The GGH selection, simplified geometry and processing are project-derived, openly reusable with attribution; no endorsement by Statistics Canada is implied. **Census indicators:** Statistics Canada, *2016 Census Profile* and *2021 Census Profile*. **Basemap:** © OpenStreetMap contributors. **Transit:** supplied RTP GIS inputs; rights to redistribute their separate source files have not been verified.
