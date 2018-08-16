# Conversion Tool Motivation

Most GOES-16 Level 2 (L2) products are written to a scaled satellite scan angle rather than a map projection. While this helps reduce filesizes, the resulting image is not georeferenced and will project to a "flat" cartesian x,y grid. This requires a work around to geolocate data and save the result as a netCDF file.

# Description
This program converts GOES-16 L1b and L2 products netCDF files from the fixed grid radian scan angle coordinates to their corresponding latitude longitude projection. The result is then re-saved in a more easily viewed NetCDF file.

Converting files occurs in three simple steps:
1. Download and place files that you wish to display in the input folder.
2. Run the python script to convert files.
3. Check the output file for the results.

## Getting Started
### Prerequisites
This is a python script, so you will need python on your computer to run this code. If you don't know where to start, I suggest installing [Anaconda Python](https://anaconda.org/anaconda/python).

### Install Libraries
There are several required python libraries. The easiest way to install the libraries is to open the terminal on your respective OS:

* Windows: search for the "Anaconda Prompt" on your local computer or find it manually in your list of programs.

* Mac: open the terminal.

Then type the code below:
```
pip install -r requirements.txt
```
You will only need to this once ever on your machine or python environment.

## Running
### Step 1: Place a file that you want to convert into the “input folder”
Before doing anything, you need to have ABI L2 NetCDF files. Place the files that you wish to convert into the input folder. Keep in mind that it may take a few longer to run the first time while navigation look-up tables are being generated and saved.

Note: If more than one file of the same product and region are placed in the input folder, they will be combined into a single file.
### Step 2: Run the script

#### Option 1: Command line
Open the terminal on your respective OS:
* Windows: search for the "Anaconda Prompt" on your local computer or find it manually in your list of programs.

* Mac: open the terminal.

You can run the script via the Anaconda Prompt or terminal by typing:
```
python main_input_output.py
```

#### Option 2: Run in the Spyder development environment
Open the Anaconda Navigator, run Spyder, and then open the main_input_outpu.py script. You can simply press the big "Play" button at the top to run the script.

### Step 3: Check the Output
Finished files will be saved in as ABI-[product name][region]-converted.nc

## Useful NetCDF viewing tools

* [Panoply](https://www.giss.nasa.gov/tools/panoply/)

## Author

* **Rebekah Esmaili** [rebekah.esmaili@gmail.com](mailto:rebekah.esmaili@gmail.com)

## More Information

* GOES-16 input data can be downloaded from NOAA's [Comprehensive Large Array-data Stewardship System (CLASS)](https://www.class.noaa.gov/).
* A detailed description of the coordinate system and the conversion to a map project can be found in Section 4.2 of the [Product Definition and Users Guide, Vol. 5](www.goes-r.gov/products/docs/PUG-L2+-vol5.pdf).
* At the time of writing, some of GOES-16 L2 products are in the *Beta Phase*. Data are preliminary and cannot be used for scientific research or operational use.
* Additional information on GOES-16 products can be found in the [Algorithm Theoretical Basis Documents (ATBD)](http://www.goes-r.gov/resources/docs.html).
