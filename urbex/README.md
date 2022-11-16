[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/szucshey/osm-data-exploration/blob/main/urbex/urbex.ipynb)

## Data source
The urbex community is a relatively closed one. Not many people likes to share locations, being afraid of vandals mostly, trying to keep the locations as intact as possible.
Of course, there are groups where they freely exchange information with each other. The data used in this notebook was collected from such groups (e.g. Facebook).

## Methodology
Every location is marked with a marker. A marker's color is determined by how safe is a location to visit (free to visit, guarded, etc.), and its icon is determined by the type of the location (military, industrial, religious, etc.)
Every marker displays a popup window when clicked, displaying further informations, and a simple gallery of a few pictures. The images are within the `images` folder. Every row of the CSV contains the corresponding folder name for its images.

## Good to know
For unknown reasons the combined size of pictures contained in a marker cant be higher than 1MB, otherwise the popup window will be blank.
