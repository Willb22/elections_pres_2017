import pandas as pd
import numpy as np
import  random
import matplotlib.pyplot as plt
import overpass
#api = overpass.API()
import re
from string import punctuation
import time
import folium
from folium import plugins
import folium.plugins as plugins


coord = pd.read_csv("../../simu_files/coord_communes2020-05-05 17:32:28.546976.csv")
coord = coord.dropna
print(type(coord['latitude']))
#print(type(coord['latitude'].iloc[6]))


lat_max = coord['latitude'].mean() + coord['latitude'].std()
lat_min = coord['latitude'].mean() - coord['latitude'].std()
long_max = coord['longitude'].mean() + coord['longitude'].std()
long_min = coord['longitude'].mean() - coord['longitude'].std()

#print(lat_min, lat_max, long_min, long_max)


map = folium.Map(location=[0,0], zoom_start=1.5, tiles = 'Stamen Toner')
#map.fit_bounds([[52.193636, -2.221575], [52.636878, -1.139759]])
map.fit_bounds([[lat_min, long_min], [lat_max, long_max]])


incidents = folium.map.FeatureGroup()

for lat, lng, in zip(coord['latitude'], coord['longitude']):
    if lat == 'NaN':
        continue

    if lng == 'NaN':
        continue

    folium.Marker(
        location=[lat, lng],
        icon=None,
        # popup=label,
    ).add_to(incidents)


marker_cluster = plugins.MarkerCluster().add_to(map)
#marker_cluster = MarkerCluster().add_to(m)
marker_cluster

for point in range(0, len(locationlist)):
    folium.Marker(locationlist[point], popup=dfn['Libellé de la commune'].iloc[point]).add_to(marker_cluster)


print(map)