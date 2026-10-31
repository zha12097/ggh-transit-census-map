/* Minimal Leaflet stand-in. Does not test real basemap or Leaflet rendering. */

window.L = {
 map: ()=>({layers:new Set(),panes:{},setView(){return this},fitBounds(){return this},getZoom(){return 9},getSize(){return {x:1500,y:950}},latLngToContainerPoint(latlng){return {x:(latlng[1]+82)*340,y:(46-latlng[0])*280}},createPane(pane){this.panes[pane]={style:{}}},getPane(pane){return this.panes[pane]},on(){return this},hasLayer(layer){return this.layers.has(layer)},addLayer(layer){this.layers.add(layer);return this},removeLayer(layer){this.layers.delete(layer);return this}}),
 tileLayer: ()=>({addTo(map){map.addLayer(this);return this}}),latLngBounds:(coords)=>coords,divIcon:(options)=>options,
 marker:(latlng,options)=>({latlng,options,addTo(group){group.addLayer(this);return this}}),
 layerGroup: ()=>({layers:[],addTo(map){map.addLayer(this);return this},addLayer(layer){this.layers.push(layer)},getLayers(){return this.layers},clearLayers(){this.layers=[]}}),
 circleMarker:(latlng,opts)=>mkLayer('point',latlng),
 geoJSON:(data,opts)=>{
  const group={_layers:[],addTo(map){map.addLayer(this);return this},getLayers(){return this._layers},eachLayer(fn){this._layers.forEach(fn);return this},getBounds(){return [[42.7,-81],[45,-77.5]]},resetStyle(layer){return this},clearLayers(){this._layers=[]},setStyle(fn){this._layers.forEach(layer=>layer.setStyle(typeof fn==='function'?fn(layer.feature):fn));return this}};
  for (const feature of data.features){
   if(opts.filter&&!opts.filter(feature))continue;
   const layer=opts.pointToLayer?opts.pointToLayer(feature,feature.geometry.coordinates):mkLayer(feature.geometry.type,null);
   layer.feature=feature;
   if(opts.style)layer.setStyle(typeof opts.style==='function'?opts.style(feature):opts.style);
   group._layers.push(layer);opts.onEachFeature(feature,layer);
  }
  return group;
 },
};
function mkLayer(kind,coords){return {kind,coords,options:{},bindPopup(arg){this.popup=arg;return this},bindTooltip(){return this},isPopupOpen(){return false},on(event,fn){(this.handlers ||= {})[event]=fn;return this},setStyle(o){Object.assign(this.options,o);return this},getLatLng(){return this.coords},getBounds(){return [[43,-80],[44,-79]]},openPopup(){return this}};}
