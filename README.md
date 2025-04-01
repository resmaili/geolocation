# Geolocation Look-up Tables
## Description
This program creates a geolocation file for GOES-16 L1b and L2 datasets. The native netCDF files contain fixed grid radian scan angle coordinates and this program calculates the corresponding latitude longitude projection fo each pixel. The result is then re-saved in a more easily viewed NetCDF file.

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

## Running

### Step 1: Update the path of the file that you want to convert in the "filename" variable
Before doing anything, you need to have ABI L2 NetCDF files. At the bottom the program, under main(), you can update the filename variable. Change the outname variable to something meaningful (should indicate if it's L1 or L2, CONUS or FD, the satellite, date generated, etc). It may take a few minutes to run, particularly with high-resolution fulldisk products.

Note: On Mac/Linux, the paths are written with a forward slash (/) whereas on PCs, it's written with two backslashes (\\\\)

### Step 2: Run the script

#### Option 1: Command line
Open the terminal on your respective OS:
* Windows: search for the "Anaconda Prompt" on your local computer or find it manually in your list of programs. You will need to write the full path of the python script (including to the input files). You may have to manually tell Windows to associate python with \*.py files.

* Mac: open the terminal.

You can run the script via the Anaconda Prompt or terminal by typing:
```
python main.py
```

#### Option 2: Run in the Spyder development environment
Open the Anaconda Navigator, run Spyder, and then open the main.py script. You can simply press the big "Play" button at the top to run the script.

### Step 3: Check the Output
Finished files will be saved in as latlon-[L1b/L2]\_[conus/fulldisk].nc

To check the results, NetCDF files can be easily viewed using [Panoply](https://www.giss.nasa.gov/tools/panoply/).

## Author
* **Rebekah Bradley Esmaili** [rebekah.esmaili@gmail.com](mailto:rebekah.esmaili@gmail.com)

## More Information

* GOES L1b and L2 data can be downloaded from the [Registry of Open Data on AWS](https://registry.opendata.aws/noaa-goes/) or NOAA's [Comprehensive Large Array-data Stewardship System (CLASS)](https://www.class.noaa.gov/)
* A detailed description of the coordinate system and the conversion to a map project can be found in Section 4.2 of the [Product Definition and Users Guide, Vol. 5](www.goes-r.gov/products/docs/PUG-L2+-vol5.pdf).
* Additional information on GOES products can be found in the [Algorithm Theoretical Basis Documents (ATBD)](http://www.goes-r.gov/resources/docs.html).
