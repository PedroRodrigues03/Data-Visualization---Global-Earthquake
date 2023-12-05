import json

# Explore the structure of the data
FILENAME = 'data/eq_data_1_day_m1.json'
with open(FILENAME) as file:
    all_eq_data = json.load(file)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as file:
    json.dump(all_eq_data, file , indent=4)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)