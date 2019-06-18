from osgeo import gdal
import glob
import os

tif_files = glob.glob('/home/rishu/vaari/Projects/1000/bindusen/s1/tif/*.tif')

for tif_file in tif_files:
	try:
		gdal.Open(tif_file).GetRasterBand(1)
	except:
		os.remove(tif_file)