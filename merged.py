#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 21:29:29 2022

@author: lymenbae
"""

import geopandas as gpd
import pandas as pd
import os
#  Set up names of files
reg_zip = "ukr_adm_sspe_20220131 (1).zip"
reg_shp = "ukr_admbnda_adm2_sspe_20220114.shp"
con_csv = "control_latest2.csv"
outfile = "by_region.gpkg"
#%%

#  Read the file of control data and set missing control entries to
#  MISSING for convenience later.

control = pd.read_csv(con_csv,dtype=str)
con_cols = [
    'geonameid',
    'name',
    'asciiname',
    'alternatenames',
    'longitude',
    'latitude',
    'feature_code'
    ]
control.set_index(con_cols,inplace=True)
control.fillna('MISSING',inplace=True)
control = control.reset_index().copy() # this resets the original index to be converted into a column
#reset_index in pandas is used to reset index of the dataframe object to default indexing (0 to number of rows minus
# or to reset multi level index
#%%

#  Build a GeoSeries from the coordinates in control file

lat = control['latitude']
lon = control['longitude']
geo = gpd.points_from_xy(lon,lat,crs="EPSG:4326")
#
#  Use the points to create a GeoDataFrame
#
control_geo = gpd.GeoDataFrame(data=control,geometry=geo)
#%%

#  Read the administrative boundaries, trim the columns, and join
#  the result onto the control points

regions = gpd.read_file(f"{reg_zip}!{reg_shp}")
joined = control_geo.sjoin(regions,how='inner',predicate='within')
joined = joined.drop(columns='index_right')
#%%

#  Select administrative and control date columns and then stack the data

reg_cols = ['ADM2_PCODE']
ctr_cols = [c for c in joined.columns if c.startswith('ctr_')]
trimmed = joined[reg_cols+ctr_cols]
trimmed = trimmed.set_index(reg_cols)
stack = trimmed.stack()
stack = stack.reset_index()
stack = stack.rename(columns={'level_1':'ctr',0:'control'})
stack['datetime'] = stack['ctr'].str.replace('ctr_','')
#%%

#  Group the records by administrative region and control date and count them

grouped = stack.groupby(['ADM2_PCODE','datetime'])
counts = grouped['control'].apply('value_counts')
res = counts.unstack()
res = res.fillna(0)
res = res.reset_index()
#  Add a total
res['total'] = res['UA']+res['RU']+res['CONTESTED']+res['MISSING']
#%%

#  Create the output file: a geopackage with layers for selected dates

if os.path.exists(outfile):
    os.remove(outfile)
#  Use these dates
dates = [
    '20220227214017',
    '20220327000910',
    '20220427001253',
    '20220522092908',
    '20220605180007'
    ]
#  Build a layer for each one
for date in dates:
    subset = res[ res['datetime'] == date ]
    geo = regions.merge(subset,
                        on='ADM2_PCODE',
                        how='outer',
                        validate='1:1',
                        indicator=True)
    layer_name = str( pd.to_datetime(date) )  
    print('\nmerge check for',layer_name)
    print(geo['_merge'].value_counts(),flush=True)
    geo = geo.drop(columns='_merge')
    geo.to_file(outfile,layer=layer_name,index=False)
    print('layer written',flush=True)
#%%
import imageio 
import os
#
#  Set output file, duration each image will be shown,
#  and the number of times the images should loop
#
outfile = 'animate.gif'
dur_time = 0.5
loop_count = 1
#
#  Read all images that start with 2022 and end with .png
#
files = []
for f in os.listdir():
    if f.startswith('Map of UA') and f.endswith('.png'):
        files.append(f)
#
#  Open the output file
#
writer = imageio.get_writer(outfile,
                            duration=dur_time,
                            loop=loop_count,
                            mode='I')
#
#  Read each image and add it to the output file
#
for f in sorted(files):
    print('adding',f,flush=True)
    image = imageio.imread(f)
    writer.append_data(image)