# Publishing and validation

## Fresh public repository

1. Create a **public** repository named `ggh-transit-census-map`, leaving the initial README/`.gitignore` options unchecked.
2. Upload the **contents** of the provided clean-repository folder, not the ZIP file or the containing folder.
3. Verify that `index.html` and `README.md` appear at the repository root. Include the hidden `.nojekyll`, `.gitignore` and `.github/workflows/check.yml` files when using a browser uploader.
4. Under **Settings → Pages**, choose **Deploy from a branch**, branch **main**, folder **/(root)**, and save.
5. Visit `https://zha12097.github.io/ggh-transit-census-map/` and verify display, filters and 2016/2021 indicators. If the page appears stale, use a hard refresh.

No `data/` folder or separate source datasets should be uploaded. The website is contained entirely in `index.html`. The public displayed information in that HTML remains extractable.

## Static checks

Requires Python 3.10+ and the open-source Shapely package. On a local computer:

```bash
python -m pip install 'shapely>=2'
python tests/check_map.py
```

The workflow in `.github/workflows/check.yml` runs these checks on new commits to GitHub. It does not require separate GIS or Census data files.

## Browser interaction smoke test (optional)

The optional mocked-Leaflet test exercises UI logic without external tile requests. Install Playwright and its Chromium browser:

```bash
python -m pip install playwright
python -m playwright install chromium
python tests/test_interactions.py
```

**Limit:** this substitutes a small Leaflet test double; it does not demonstrate that the real Leaflet library, external CDN, public OpenStreetMap tiles or browser rendering work. Always conduct a manual test on the deployed GitHub Pages site, especially at 0%, 50% and 100% municipal fill opacity.

## Release smoke test

- Transit points and routes display and respond to Project Status **All/None** and technology filters.
- The Census year buttons and each of the three indicator selectors update polygon colouring, legend and readout.
- The municipal fill slider defaults to 100%, which fully hides the basemap **inside** the polygons; at 0%, the fill is transparent but the outlines remain opaque.
- Municipal names and the basemap toggle independently; Reset restores the default filters, year, opacity and visibility.
- The map loads on a phone-sized viewport and remains usable with the filter drawer.

## Prior public repository and historical uploads

If the previous public repository contained separate source datasets, deleting them with an ordinary commit does not eliminate them from historical commits. Recreating a repository of the same name provides a fresh visible commit history but **cannot undo clones, forks, prior downloads or every GitHub-retained copy**. Review the earlier repository's history and GitHub's retention/recovery policies before treating the data as unavailable elsewhere.
