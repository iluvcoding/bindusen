#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 18:42:32 2018

@author: tomer
"""

from sentinelsat.sentinel import SentinelAPI
#import datetime as dt
import os

def download_s2(user, password, dir_raw, dir_nc, start_date, end_date, footprint, pr_status):


    api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus/')
    
    #footprint = "POLYGON((73 11, 74 11, 74 14, 73 14, 73 11))"
    #products = api.query(footprint, date=(start_date, end_date), producttype='S2MSI1C')
    products = api.query(footprint, date=(start_date, end_date), 
                         producttype='S2MSI1C',cloudcoverpercentage = (0,20))

   
    #print(products)
    
    l = ['S2A_MSIL1C_20180601T051651_N0206_R062_T43PFN_20180601T082308', 'S2A_MSIL1C_20180621T051651_N0206_R062_T43PFN_20180621T081647', 'S2B_MSIL1C_20180613T050649_N0206_R019_T43PFN_20180613T084228',
         'S2A_MSIL1C_20180601T051651_N0206_R062_T43PFP_20180601T082308', 'S2A_MSIL1C_20180621T051651_N0206_R062_T43PFP_20180621T081647', 'S2B_MSIL1C_20180613T050649_N0206_R019_T43PFP_20180613T084228',
         'S2A_MSIL1C_20180608T050651_N0206_R019_T43PFN_20180608T084904', 'S2A_MSIL1C_20180628T050651_N0206_R019_T43PFN_20180628T081023', 'S2B_MSIL1C_20180616T051649_N0206_R062_T43PFN_20180616T090733',
         'S2A_MSIL1C_20180608T050651_N0206_R019_T43PFP_20180608T084904', 'S2A_MSIL1C_20180628T050651_N0206_R019_T43PFP_20180628T081023', 'S2B_MSIL1C_20180616T051649_N0206_R062_T43PFP_20180616T090733',
         'S2A_MSIL1C_20180611T051651_N0206_R062_T43PFN_20180611T081245', 'S2B_MSIL1C_20180603T050649_N0206_R019_T43PFN_20180603T084545', 'S2B_MSIL1C_20180623T050649_N0206_R019_T43PFN_20180623T084444',
         'S2A_MSIL1C_20180611T051651_N0206_R062_T43PFP_20180611T081245', 'S2B_MSIL1C_20180603T050649_N0206_R019_T43PFP_20180603T084545', 'S2B_MSIL1C_20180623T050649_N0206_R019_T43PFP_20180623T084444',
         'S2A_MSIL1C_20180618T050651_N02206_R019_T43PFN_20180618T085607', 'S2B_MSIL1C_20180606T051649_N0206_R062_T43PFN_20180606T104751', 'S2B_MSIL1C_20180626T051649_N0206_R062_T43PFN_20180626T090058',
         'S2A_MSIL1C_20180618T050651_N0206_R019_T43PFP_20180618T085607', 'S2B_MSIL1C_20180606T051649_N0206_R062_T43PFP_20180606T104751', 'S2B_MSIL1C_20180626T051649_N0206_R062_T43PFP_20180626T090058']
    
    for product in products:
        productInfo = api.get_product_odata(product)
        title = productInfo['title']
        
        
        if title in l:
            continue
        
        tileNo_time = '%s_%s' % (title.split('_')[5], title.split('_')[2])
    
        try:
            downloadFlag = not pr_status[tileNo_time]
        except KeyError:
            pr_status[tileNo_time] = False
            downloadFlag =True
            print "no error"
        #file_nc = os.path.join(dir_nc, "%s_VV.nc"%os.path.basename(title).split("_")[4])
        #file_nc = os.path.join(dir_nc, "%s_VV.nc" % title[17:48])
        file_wkt = os.path.join(os.path.dirname(dir_nc), "wkt/%s.wkt" % tileNo_time)
                
        if not os.path.exists(file_wkt):
            pFootPrint = productInfo['footprint']
            file = open(file_wkt, "a")
            file.write(pFootPrint)
            file.close()
        
        if downloadFlag and not title in l:
            
            api.download(product, dir_raw, checksum=True)
            l.append(title)
        
        return pr_status