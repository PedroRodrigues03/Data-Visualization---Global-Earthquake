import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data
FILENAME = 'data/eq_data_1_day_m1.json'
with open(FILENAME) as file:
    all_eq_data = json.load(file)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as file:
    json.dump(all_eq_data, file , indent=4)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Map the earthquakes
data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_texts,
    'marker' : {
        'size' : [5 * mag for mag in mags],
        'color' : mags,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title' : 'Magnitude'}
    },
}]

map_title = all_eq_data['metadata']['title']
my_layout = Layout(title=map_title)
fig = {
    'data' : data,
    'layout' : my_layout,
}

offline.plot(fig, filename='html/global_earthquakes.html')