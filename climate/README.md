[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/szucshey/osm-data-exploration/blob/main/climate/climate.ipynb)

# Visualizing daily weather data in Hungary

## Data source
The data for this topic is provided by the [E-OBS dataset](https://cds.climate.copernicus.eu/cdsapp#!/dataset/insitu-gridded-observations-europe?tab=overview). 
The data comes in NetCDF4 format, and covers the whole of Europe.
Considering, that most of the data is unneccessary in this case, I've masked the datasets for a rectangle, that covers the area of Hungary. 
These masked datasets were uploaded to the datasets folder.
The complete dataset spans in time from 1950 to 2021, but it is sliced in 5 files.

## Visualization via matplotlib
For every day represented by the dataset a matplotlib figure is created, and gets rendered as an image.
The values belonging to each coordinate are mapped on a colormap.

After the images are rendered, they can be saved as a GIF using Pillow.

### Good to know
Always set the `start_date` variable to the first date contained by the dataset you're currently working on.

You can change the colormap to your liking. The `vmin` and `vmax` parameters represent the ends of a colormap.
Matplotlib's built-in colormaps can be found [here](https://matplotlib.org/stable/tutorials/colors/colormaps.html).

When saving a GIF, the `duration` parameter sets the length of a frame in milliseconds

## Visualization via Blender
The provided `render_map.py` script is made to render a 3D topographic map of Hungary.

The script has to be imported into Blender (version 3.3.1 or higher) and executed from there.

Using Overpass, I've requested the country borders, and filtered the coordinates that are within the area of the country.

Using [Open-Elevation's public API](https://open-elevation.com/), I've created `elevation.csv` found under the datasets folder, storing the elevation of each coordinate.

The script generates a column in each coordinate's location, with the height being determined by the corresponding elevation.
The color of a column is determined by a colormap just like previously detailed.

A Camera object is rotated around the map. The `frames` variable determines how many keyframes does it take for the camera to complete a full circle around the map.
The keyframes then are rendered as a GIF using Pillow.
