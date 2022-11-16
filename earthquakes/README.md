[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/szucshey/osm-data-exploration/blob/main/earthquakes/earthquakes.ipynb)

# Visualizing earthquakes around Europe

## Data source
The dataset was downloaded from the [USGS Earthquake Catalog](https://earthquake.usgs.gov/earthquakes/search/).
You can query data by multiple criteria, but one request may only return 20000 lines tops, hence this topic only covers earthquakes that happened between 2010 and 2022, with a minimum magnitude of 1.5.

## Methodology
For every row in the CSV file a marker is added to the right coordinates, both the radius and the color is determined by the magnitude of the earthquake.
Each marker displays a tooltip on click, revealing additional information.
