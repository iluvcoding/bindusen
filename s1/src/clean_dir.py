#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:16:09 2018

@author: tomer
"""

import glob
import os
#import numpy as np
import shutil

def delete_file_fun(delete_files):
    delete_files = glob.glob(delete_files)
    for delete_file in delete_files:
        if os.path.exists(delete_file):
            try:
                os.remove(delete_file)
                print("%s deleted"%delete_file)
            except OSError:
                shutil.rmtree(delete_file)
                print("%s deleted"%delete_file)
            
            
def clean_dir(yyyymmdd, dir_raw, dir_dim, dir_nc, dir_tif):
    
    file_vvs = glob.glob(os.path.join(dir_nc, "S1?_??_????_????_%sT*_VV.nc"%yyyymmdd))
    for file_vv in file_vvs:
        file_vh = file_vv.replace("VV","VH")
        file_ia = file_vv.replace("VV","IA")
        file_la = file_vv.replace("VV","LA")
        ncFlags = os.path.exists(file_vv) and os.path.exists(file_vh) and os.path.exists(file_ia) and os.path.exists(file_la) 
        if ncFlags:
            # file name for tif
            delete_file_fun(os.path.join(dir_tif, os.path.basename(file_vv).replace(".nc", ".tif")))
            delete_file_fun(os.path.join(dir_tif, os.path.basename(file_vh).replace(".nc", ".tif")))
            delete_file_fun(os.path.join(dir_tif, os.path.basename(file_la).replace(".nc", ".tif")))
            delete_file_fun(os.path.join(dir_tif, os.path.basename(file_ia).replace(".nc", ".tif")))
            # file name for dim
            foo = os.path.basename(file_vv)[:-7]
            delete_file_fun(os.path.join(dir_dim,"*%s*.dim"%foo))
            delete_file_fun(os.path.join(dir_dim,"*%s*.data"%foo))
            #    delete_file_fun(dataFile)
            
            # file name for zip
            print glob.glob(os.path.join(dir_raw,"*%s*.zip"%foo))
            
            #print os.path.basename(file_vv).split("_")[0]
    
