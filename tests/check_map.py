#!/usr/bin/env python3
"""Static QA of a self-contained GGH map. Shapely>=2 required; no private data inputs."""
from pathlib import Path
import json, re, hashlib
from shapely.geometry import shape

ROOT=Path(__file__).resolve().parents[1]
source=ROOT/'index.html'
html=source.read_text(encoding='utf-8')

def read_json(name):
    m=re.search(r'(?m)^const '+re.escape(name)+r' = (.*);$',html)
    assert m, 'Inline dataset absent: '+name
    return json.loads(m.group(1))

municipalities=read_json('municipalitiesData')['features']
points=read_json('pointsData')['features']
routes=read_json('routesData')['features']
profiles16=read_json('census2016ByCode')
assert (len(municipalities),len(points),len(routes))==(99,387,127)
csds=[str(f['properties']['census_csd']) for f in municipalities]
assert len(set(csds))==99
assert set(csds)==set(profiles16)
keys16={tuple(sorted(rec.keys())) for rec in profiles16.values()}
keys21={tuple(sorted(f['properties']['census'].keys())) for f in municipalities}
assert len(keys16)==len(keys21)==1
assert keys16==keys21 and len(next(iter(keys16)))==57
for f in municipalities:
    props=f['properties']
    code=str(props['census_csd'])
    assert all(type(x) in (float,int) for x in profiles16[code].values())
    assert all(type(x) in (float,int) for x in props['census'].values())
    assert shape(f['geometry']).is_valid, 'Invalid geometry: '+props['NAME_E']
assert 'let municipalFillOpacity=1;' in html
assert 'fillOpacity:municipalFillOpacity' in html
assert "opacity:1" in html
assert "https://tile.openstreetmap.org/{z}/{x}/{y}.png" in html
assert 'class="status-select"' in html
assert 'id="basemapOn"' in html
assert 'id="municipalityOpacity"' in html
assert 'id="censusYear2016"' in html and 'id="censusYear2021"' in html
print('PASS — 99 valid boundaries, 387 transit points, 127 routes')
print('PASS — 99 matched CSDs and 57 numeric indicators for 2016 and 2021')
print('PASS — OSM basemap, fill-opacity slider and filter controls present')
print('SHA-256:',hashlib.sha256(source.read_bytes()).hexdigest())
