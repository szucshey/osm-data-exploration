[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/szucshey/osm-data-exploration/blob/main/covid/covid-data-visualization.ipynb)

# Visualizing COVID-19 data in Hungary

## Data source
Ever since the breakout in early 2020, the official communication about the virus was through [koronavirus.gov.hu](https://koronavirus.gov.hu/) from the government's side.
Problem is, the data is overwritten every day, there is no official archived dataset.

Luckily, the guys over at [Koronamonitor](https://atlo.team/koronamonitor/) have been collecting data every day from the very start of the pandemic.

Only the number of infected people have been published regionally, so only this dataset can be visualized on maps.

## Methodology
The required administrative borders are requested from OpenStreetMap using Overpass.

Using these borders filtered to one day, an interactive choropleth map is made, with tooltips displaying further information on hover.
Further layers can be added to the map, visualizing different data.

Using folium's TimeSliderChoropleth plugin, a map is created with an interactive slider that can control the displayed date.

![TimeSliderChoropleth GIF](https://media.giphy.com/media/2ELmrswPJgPV3qgs8q/giphy-downsized-large.gif)
