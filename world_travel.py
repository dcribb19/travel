# world_travel.py
# Create an overlay on world map of countries that you have traveled to.

import folium
import os
import json

# initialize map
m = folium.Map(location=[39.833333, -50],
               tiles='CartoDB positron',
               min_zoom=2,
               zoom_start=2,
               min_lon=-180,
               max_lon=180,
               max_bounds=True)

world = os.path.join(os.getcwd(), 'world-countries.json')


def get_country_names():
    '''Return a list of country names from world json file.'''
    with open(world) as file:
        countries = json.load(file)
    return [countries['features'][x]['properties']['name']
            for x in range(len(countries['features']))]


def style(person, color):
    """
    take a person's name and a color to fill in countries traveled to
    """
    return lambda x: {'fillColor': color if x['properties']['name']
                      in person['Countries'] else 'white',
                      'color': 'black',
                      'weight': 0.3,
                      'fillOpacity': 0.5 if x['properties']['name']
                      in person['Countries'] else 0.0
                      }


def countries_traveled(person, color):
    folium.GeoJson(data=world,
                   name=person['Name'] + ' - '
                   + str(len(person['Countries'])),
                   style_function=style(person, color)
                   ).add_to(m)


'''
EXAMPLE CODE:

person_1 = {
    'Name' : 'Person 1',
    'Countries' : ['Spain', 'Chile', 'Australia', 'Peru', 'China']
}

countries_traveled(person_1, 'red')
'''

folium.LayerControl(hideSingleBase=True).add_to(m)
m.save('world_map.html')
