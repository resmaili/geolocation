#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import join, exists, dirname, abspath, basename
from netCDF4 import Dataset
import numpy as np
from tqdm import tqdm

def get_abi_2d_lat_lon_coordinates(file_id, outname):
    # Re-maps x, y into lat/lon projection, saves file for future use/faster processing.

    bytescale_x_vector = file_id.variables['x'][:]
    x_scale_factor = file_id.variables['x'].scale_factor
    x_offset = file_id.variables['x'].add_offset

    bytescale_y_vector = file_id.variables['y'][:]
    y_scale_factor = file_id.variables['y'].scale_factor
    y_offset = file_id.variables['y'].add_offset

    sub_lon = file_id.variables['goes_imager_projection'].longitude_of_projection_origin
    sub_lat = file_id.variables['goes_imager_projection'].latitude_of_projection_origin

    xdim = len(bytescale_x_vector)
    ydim = len(bytescale_y_vector)

    latitude = np.zeros((ydim, xdim))
    longitude = np.zeros((ydim, xdim))
    for i, bytescale_y in enumerate(tqdm(bytescale_y_vector)):
        for j, bytescale_x in enumerate(bytescale_x_vector):
            latitude[i, j], longitude[i, j] = convert_bytescale_to_coordinates(
                bytescale_x,  bytescale_y,
                x_offset,  y_offset,
                x_scale_factor, y_scale_factor,
                sub_lon, sub_lat)

    # Save results to file to speed up future processing
    create_lat_lon_netcdf(latitude, longitude, file_id, name=outname)

def convert_bytescale_to_coordinates(column,  row,
    column_offset,  row_offset,
    column_factor, row_factor,
    sub_lon, sub_lat):

    # Python automatically applies scale factor and offset
    lamda = column
    theta = row
    y = np.arcsin( np.sin(theta)*np.cos(lamda) )
    x = np.arctan( np.tan(lamda)/np.cos(theta) )
    sat_height = 42164.16

    cos_x = np.cos(x)
    cos_y = np.cos(y)
    sin_x = np.sin(x)
    sin_y = np.sin(y)

    pix_satellite_distance = (sat_height*cos_x*cos_y)**2.0 - (cos_y*cos_y + 1.006803*sin_y*sin_y)*1737121856.0

    # Check if pixel located on Earth surface or in space (negative pixel distance values)
    if ( pix_satellite_distance <= 0.0 ):
        latitude_degrees = -999.00
        longitude_degrees = -999.00
        return latitude_degrees, longitude_degrees

    else:
        sqrt_pix_satellite_distance = np.sqrt( pix_satellite_distance )
        sn = (sat_height*cos_x*cos_y - sqrt_pix_satellite_distance) / (cos_y*cos_y + 1.006803*sin_y*sin_y)

        s1 = sat_height - sn*cos_x*cos_y
        s2 = sn*sin_x*cos_y
        s3 = 1.0*sn*sin_y

        sxy = np.sqrt( s1*s1 + s2*s2 )

        longitude_radians = np.arctan(s2/s1)
        latitude_radians  = np.arctan((1.006803*s3)/sxy)

        latitude_degrees = latitude_radians*180.0/np.pi + sub_lat
        longitude_degrees = longitude_radians*180.0/np.pi + sub_lon

        return latitude_degrees, longitude_degrees

def create_lat_lon_netcdf(latitude_2d, longitude_2d, file_id, name):
    from netCDF4 import Dataset

    missing=-999.0

    rootgrp = Dataset(name, "w", format="NETCDF4")
    rootgrp.description = "Fulldisk coordinates (degrees) for L2 GOES-17 (Test Position!)"

    lat = rootgrp.createDimension("lat", latitude_2d.shape[0])
    lon = rootgrp.createDimension("lon", longitude_2d.shape[1])

    latitudes = rootgrp.createVariable("latitude","f4",("lat","lon"), zlib=True, least_significant_digit=2)
    longitudes = rootgrp.createVariable("longitude","f4",("lat","lon"), zlib=True, least_significant_digit=2)

    # Save substellite point in file
    longitude_of_projection_origin = rootgrp.createVariable("nominal_satellite_subpoint_lon", "f8",  zlib=True, least_significant_digit=2)
    latitude_of_projection_origin = rootgrp.createVariable("nominal_satellite_subpoint_lat", "f8",  zlib=True, least_significant_digit=2)

    latitude_of_projection_origin[0] = file_id.variables['goes_imager_projection'].latitude_of_projection_origin
    longitude_of_projection_origin[0] = file_id.variables['goes_imager_projection'].longitude_of_projection_origin

    latitudes.units = "degrees north"
    longitudes.units = "degrees east"

    latitudes[:,:] = latitude_2d
    longitudes[:,:] = longitude_2d

    rootgrp.close()

def main():
    outname="latlon_L2_G17_CONUS_89W_2.nc"
    filename="OR_ABI-L2-AODC-M3_G17_s20182211612186_e20182211614557_c20182211615551.nc"

    file_id = Dataset(filename, mode='r')
    get_abi_2d_lat_lon_coordinates(file_id, outname)

main()
