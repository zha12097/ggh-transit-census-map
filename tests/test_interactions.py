#!/usr/bin/env python3
"""Headless mock-Leaflet interaction smoke test (requires playwright and Chromium)."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import re,sys
ROOT=Path(__file__).resolve().parents[1]
html=(ROOT/'index.html').read_text(encoding='utf-8')
stub=(Path(__file__).parent/'leaflet_stub.js').read_text(encoding='utf-8')
html=re.sub(r'<link rel="stylesheet" href="https://unpkg.com/leaflet@1\.9\.4/dist/leaflet\.css"[^>]*>', '',html)
html=re.sub(r'<script src="https://unpkg.com/leaflet@1\.9\.4/dist/leaflet\.js"[^>]*></script>', '<script>'+stub+'</script>',html)
with sync_playwright() as pw:
 chromium_path='/usr/bin/chromium' if Path('/usr/bin/chromium').exists() else None
 launch_args={'headless':True}
 if chromium_path:launch_args.update(executable_path=chromium_path,args=['--no-sandbox','--disable-dev-shm-usage'])
 browser=pw.chromium.launch(**launch_args)
 for width,height in ((1366,900),(390,844)):
  page=browser.new_page(viewport={'width':width,'height':height})
  errors=[];page.on('pageerror',lambda err:errors.append(str(err)))
  page.route('**/*',lambda route:route.abort())
  page.set_content(html,wait_until='domcontentloaded',timeout=30000)
  assert not errors,errors
  assert page.locator('#totalPoints').inner_text()=='387'
  assert page.locator('#totalRoutes').inner_text()=='127'
  assert page.locator('#totalMunicipalities').inner_text()=='99'
  assert page.locator('#visibleCount').inner_text()=='514'
  assert page.evaluate('municipalitiesLayer.getLayers().every(x=>x.options.opacity===1 && x.options.fillOpacity===1)')
  if width<600: page.locator('#mobilePanelToggle').click()
  slider=page.locator('#municipalityOpacity')
  for pct in (0,50,100):
   slider.fill(str(pct));slider.dispatch_event('input')
   assert page.evaluate(f'municipalitiesLayer.getLayers().every(x=>x.options.opacity===1 && x.options.fillOpacity==={pct/100})'),pct
  page.locator('.status-select[data-set="none"]').click()
  assert page.locator('#visibleCount').inner_text()=='0'
  page.locator('.status-select[data-set="all"]').click()
  assert page.locator('#visibleCount').inner_text()=='514'
  page.locator('.tech-select[data-kind="point"][data-set="none"]').click()
  assert page.locator('#visibleCount').inner_text()=='127'
  page.locator('.tech-select[data-kind="point"][data-set="all"]').click()
  assert page.locator('#visibleCount').inner_text()=='514'
  page.locator('#censusIndicatorsDetails > summary').click()
  page.locator('#censusLevelMetric').select_option('population')
  assert 'Population' in page.locator('#censusLegend').inner_text()
  page.locator('#censusYear2016').click()
  assert '2016' in page.locator('#censusLegend').inner_text()
  assert page.evaluate('municipalitiesLayer.getLayers().every(x=>x.options.fillOpacity===1 && x.options.opacity===1)')
  page.locator('#municipalityOpacity').fill('0');page.locator('#municipalityOpacity').dispatch_event('input')
  assert page.evaluate('municipalitiesLayer.getLayers().every(x=>x.options.fillOpacity===0 && x.options.opacity===1)')
  page.locator('#basemapOn').uncheck(force=True)
  assert page.evaluate('!map.hasLayer(osmBaseLayer)')
  page.locator('#basemapOn').check(force=True)
  assert page.evaluate('map.hasLayer(osmBaseLayer)')
  page.locator('#resetFilters').click()
  assert page.locator('#municipalityOpacity').input_value()=='100'
  assert page.locator('#visibleCount').inner_text()=='514'
  assert page.evaluate('municipalitiesLayer.getLayers().every(x=>x.options.fillOpacity===1 && x.options.opacity===1)')
  assert not errors,errors
  print('PASS:',width,'x',height,'(mocked Leaflet)')
  page.close()
 browser.close()
