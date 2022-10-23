from osgeo import gdal

def shapefile2geojson(infile, outfile):
    '''Translate a shapefile to GEOJSON.'''
    options = gdal.VectorTranslateOptions(format="GeoJSON",dstSRS="EPSG:4326")
    gdal.VectorTranslate(outfile, infile, options=options)

infile=r"/Users/pathaoltd/Desktop/GEO SPEKTRON/Shapefile Conversion/Dhaka latest Shapefile/Dhaka Latest Shapefile.shp"


shapefile2geojson(infile, r"/Users/pathaoltd/Desktop/GEO SPEKTRON/Shapefile Conversion/Dhaka Shapefile to GeoJSON/Dhaka_GeoJSON.geojson")