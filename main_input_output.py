#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Description
    This program converts GOES product netCDF files from 
    the fixed grid radian coordinates to their coresponding 
    latitude longitude projection. 

@Dependencies
    support_functions.py

@Inputs
    Any GOES L1b or L2 product. Products an be downloaded from 
    https://www.class.ngdc.noaa.gov.

@Outputs
    output/latlon_[L1b/L2]_[conus/fulldisk].nc

@author: Rebekah Bradley Esmaili
@email: bekah@umd.edu
"""
from netCDF4 import Dataset
#import numpy as np
from numpy import zeros
from support_functions import get_abi_value, get_adp_value, get_abi_2d_lat_lon_coordinates, detect_file_types, check_subsatellite_position
from glob import glob
from os import makedirs, getcwd
from os.path import join, exists, dirname, abspath
import sys

# Define paths
projectPath = "//"

inputPath = join(projectPath, "input")
outputPath = join(projectPath, "output")

if not exists(inputPath):
    makedirs(inputPath)
    
if not exists(outputPath):
    makedirs(outputPath)

searchForFiles = join(inputPath, "*.nc")
filenames = [basename(i) for i in glob(searchForFiles)]

geolocFiles = detect_file_types(filenames)

for filenum, geolocFile in enuemrate(geolocFiles):
    if exists(outputPath + geolocFile):
    	continue
    	
	abiFile = filenames[filenum]
	file_id = Dataset(filename, mode='r')
    latitude, longitude = get_abi_2d_lat_lon_coordinates(abiFile, geolocFile)
