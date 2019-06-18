#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:22:27 2018

@author: tomer
"""

from subprocess import call
import glob
import os
import datetime as dt

def process_snap(yyyymmdd, dir_raw, dim_dir, tif_dir, nc_dir, file_xml, path_gpt):
    
    files_zip = glob.glob(os.path.join(dir_raw, "*S1?_??_????_????_%s*.zip"%yyyymmdd))
    file_xml_temp = "IW_GRDH_1SDV.xml"
    
    # main program
    for file_zip in files_zip:
        basename = os.path.basename(file_zip)
        out_file = os.path.join(dim_dir, basename[:-4] + '.dim')
        ncLen = len(glob.glob(os.path.join(nc_dir, basename[:-4] + '_??.nc')))
        if ncLen != 4:
            tifLen = len(glob.glob(os.path.join(tif_dir, basename[:-4] + '_??.tif')))
            if tifLen != 4:
                imgLen = len(glob.glob(os.path.join(dim_dir, '%s.data' % basename[:-4], '*img')))        
                if imgLen != 4:
                    orig_f = open(file_xml, 'r')
                    f = open(file_xml_temp, 'w')
                    for line in orig_f:
                        if 'in_zip' in line:
                            line = line.replace('in_zip', file_zip)
                        if 'out_dim' in line:
                            line = line.replace('out_dim', out_file)
                        f.write(line)
                
                    f.close()
                    orig_f.close()
                
                    SC = '%s %s' % (path_gpt, file_xml_temp)
                    call(SC, shell=True)
                    print('%s processed' % file_zip)
        