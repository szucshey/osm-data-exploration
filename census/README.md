[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/szucshey/osm-data-exploration/blob/main/census/census_data_in_hungary.ipynb)

# Visualizing data from past censuses in Hungary

## Data source
The data source used in this notebook was collected and created by László Sebők.

The database is publicly accessible [here](https://mtatkki.ogyk.hu/nepszamlalas_adatok.php).

The complete dataset had to be scraped, the code is available within census_data_scrap.ipynb.

data.csv contains the processed dataset, that is used in the main notebook.

## Methodology
The required administrative borders are requested from OpenStreetMap using Overpass.

By default the notebook generates maps from only one census, and displays the distribution of the different nationalities.

The shape of each town's area gets converted to a polygon. Within this polygon a dot is generated for every N person for each nationality.
The value of N is set via the `representation` variable. Each nationality is distinctly marked with separate colors, they are stored on separate layers, only one may be visible at a time. You can toggle the layers at the bottom left corner of the rendered map.

## Good to know
Tens of thousands of dots are generated on each layer, hence both the runtime (~15 mins), both the output size (3-500MB) is large.
The notebook can't display maps of such sizes properly, the output is saved as an HTML file.

The GIF was created separately, only for demonstration purposes, you can not replicate it using only the notebook.
