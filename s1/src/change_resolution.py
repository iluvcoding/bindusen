#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 20:16:00 2018

@author: tomer
"""

import glob
import os
from subprocess import call


def translateRaster(in_ras, out_ras, res):
    SC = "gdalwarp %s %s -tr %f %f -tap"%(in_ras, out_ras, res, res)
    call(SC, shell=True)

def change_resolution(yyyymmdd, dir_dim, dir_tif, dir_nc, res):
    
    #basename = os.path.basename(file_zip)
    #out_file = os.path.join(dim_dir, basename[:32] + '.dim')
        
    dirs_in = glob.glob(os.path.join(dir_dim, "*%s*.data"%yyyymmdd))
    
    for dir_in in dirs_in:
        foo = os.path.basename(dir_in)[:-5]
        
        out_VV_nc = os.path.join(dir_nc, "%s_VV.nc"%foo)
        if not os.path.exists(out_VV_nc):
            out_VV = os.path.join(dir_tif, "%s_VV.tif"%foo)
            if not os.path.exists(out_VV):
                in_VV = os.path.join(dir_in, "Sigma0_VV.img")
                translateRaster(in_VV, out_VV, res)
        
        out_VH_nc = os.path.join(dir_nc, "%s_VH.nc"%foo)
        if not os.path.exists(out_VH_nc):
            out_VH = os.path.join(dir_tif, "%s_VH.tif"%foo)
            if not os.path.exists(out_VH):
                in_VH = os.path.join(dir_in, "Sigma0_VH.img")
                translateRaster(in_VH, out_VH, res)
            
        out_IA_nc = os.path.join(dir_nc, "%s_IA.nc"%foo)
        if not os.path.exists(out_IA_nc):
            out_IA = os.path.join(dir_tif, "%s_IA.tif"%foo)
            if not os.path.exists(out_IA):
                in_IA = os.path.join(dir_in, "incidenceAngleFromEllipsoid.img")
                translateRaster(in_IA, out_IA, res)
        
        out_LA_nc = os.path.join(dir_nc, "%s_LA.nc"%foo)
        if not os.path.exists(out_LA_nc):
            out_LA = os.path.join(dir_tif, "%s_LA.tif"%foo)
            if not os.path.exists(out_LA):
                in_LA = os.path.join(dir_in, "localIncidenceAngle.img")
                translateRaster(in_LA, out_LA, res)
        
        print(foo)
    