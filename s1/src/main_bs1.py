#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 18:32:06 2018

@author: tomer
"""

import os
import getpass
import datetime as dt
    
from download_s1 import download_s1
from process_snap import process_snap
from change_resolution import change_resolution
from convert_nc import convert_nc
from clean_dir import clean_dir
#from mosaic_tifs import mosaic_tifs
import sentinelsat
############ System specific inputs #######################
username = getpass.getuser()
if username == "satyukt":
    dir_vaari = "/media/satyukt/vaari/Projects/1000/bindusen/s1/"
    path_gpt = "/home/satyukt/Tools/snap/bin/gpt"
elif username == "rishu":
    dir_vaari = "/home/rishu/Projects/1000/bindusen/s1/out_vaari_mount/"
    path_gpt = "/home/satyukt/Tools/snap/bin/gpt"
    

################ Generic inputs ############################cd
res = 0.00018 # in degree

user = 'rishabhmehta'
password = 'rishu123'
dir_raw = os.path.join(dir_vaari, "raw_data")
dir_dim = os.path.join(dir_vaari, "dim")
dir_tif = os.path.join(dir_vaari, "tif")
dir_nc = os.path.join(dir_vaari, "nc")
#dir_mosaic = os.path.join(dir_vaari, "mosaic")
dir_src = os.path.dirname(os.path.realpath(__file__))
file_xml = os.path.join(dir_src, 'IW_GRDH_1SDV_orig2.xml')

dir_project = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
file_area = os.path.join(dir_project, "area", "united_kingdom_small.csv") 

file = open(file_area, "r") 
footprint = file.read()
file.close()
###### main #############################

start_date = dt.date(2016,6,1)
end_date = dt.date(2018,12, 3) # Changed by thiyaku
#end_date = dt.date(2018,12,31)
#end_date = dt.date.today()
ndays = (end_date - start_date).days + 1

for td in range(ndays):
    #cur_dt = start_date + dt.timedelta(days=td)
    cur_dt = end_date - dt.timedelta(days=td)
    dt1 = cur_dt + dt.timedelta(days=1)
    yyyymmdd = "%s%02d%02d"%(cur_dt.year, cur_dt.month, cur_dt.day)
    yyyymmdd1 = "%s%02d%02d"%(dt1.year, dt1.month, dt1.day)
    print(yyyymmdd)
    
    #try:
    download_s1(user, password, dir_raw, dir_nc, yyyymmdd, yyyymmdd1, footprint)
    # delay = 60 + random.random() * random.randint(1,10)   
    #time.sleep(delay)
    process_snap(yyyymmdd, dir_raw, dir_dim, dir_tif, dir_nc, file_xml, path_gpt)
    change_resolution(yyyymmdd, dir_dim, dir_tif, dir_nc, res)
    convert_nc(yyyymmdd, dir_tif, dir_nc)
    clean_dir(yyyymmdd, dir_raw, dir_dim, dir_nc, dir_tif)
    #except:
    #    print('Error')
    #    print dir_nc

    print(yyyymmdd)
    #break
