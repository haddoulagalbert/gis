import sys
from osgeo import ogr

'''
input_shp: path of the shapefile containing the features
field_name: field values that will be use rename the output shapefiles
folder: folder in which the output shapefiles will be saved
'''
def features_to_shp(input_shp, field_name, folder):

	driver = ogr.GetDriverByName('ESRI Shapefile')
	input_ds = driver.Open(input_shp)
	
	if input_ds is None:
		print("Couldn't open shapefile")
		sys.exit()
	
	layer = input_ds.GetLayer()

	for feature in layer:
		
		field = feature.GetFieldAsString(field_name)
		
		output_shp = folder+field+'.shp'
		
		output_ds = driver.CreateDataSource(output_shp)
		
		newLayer = output_ds.CreateLayer(field, geom_type = ogr.wkbPolygon)
		newLayerDef = newLayer.GetLayerDefn()
		
		geom = feature.GetGeometryRef()
		
		newFeature = ogr.Feature(newLayerDef)
		newFeature.SetGeometry(geom)
		
		newLayer.CreateFeature(newFeature)
		
		output_ds.Destroy()
		
	input_ds.Destroy()
		
