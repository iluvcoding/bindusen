#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 18:42:32 2018

@author: tomer
"""

from sentinelsat.sentinel import SentinelAPI
import datetime as dt
import os

def download_s1(user, password, dir_raw, dir_nc, start_date, end_date, footprint):
    

    api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus/')
    
    #footprint = "POLYGON((73 11, 74 11, 74 14, 73 14, 73 11))"
    products = api.query(footprint, date=(start_date, end_date), producttype='GRD')
    
    #print(products)
    
    for product in products:
        productInfo = api.get_product_odata(product)
        title = productInfo['title']
        
        print(title)
        file_nc = os.path.join(dir_nc, "%s_VV.nc" % title)
        file_wkt = os.path.join(os.path.dirname(dir_nc), 'wkt', "%s.wkt" % title)
        
        if not os.path.exists(file_wkt):
            pFootPrint = productInfo['footprint']
            file = open(file_wkt, "a")
            file.write(pFootPrint)
            file.close()
        if not os.path.exists(file_nc):
            api.download(product, dir_raw, checksum=True)
        
