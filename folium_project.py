import gdal

def shapefile2geojson(infile, outfile, fieldname):
    '''Translate a shapefile to GEOJSON.'''
    options = gdal.VectorTranslateOptions(format="GeoJSON",
                                          dstSRS="EPSG:4326")
    gdal.VectorTranslate(outfile, infile, options=options)
