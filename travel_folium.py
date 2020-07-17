# travel.py
# Create a personal overlay on the U.S. map of states traveled to.

import folium
import os

state_geo = os.path.join(os.getcwd(), 'us-states.json')

#initialize map
us_map = folium.Map(location=[39.833333, -98.583333],
                    tiles='CartoDB positron',
                    min_zoom=4,
                    max_zoom=7,
                    zoom_start=4,
                    min_lat=10,
                    max_lat=72,
                    min_lon=-180,
                    max_lon=-40,
                    max_bounds=True,
                   )


def state_style(person, color):
    """
    take a person's name and a color to fill in states traveled to
    """
    return lambda x: {'fillColor': color if x['id']
                      in person['States'] else 'white',
                      'color': 'black',
                      'weight': 0.3,
                      'fillOpacity': 0.5 if x['id']
                      in person['States'] else 0.0
                     }


def states_traveled(person, color):
    """
    Take a person's name and a color to create GeoJson overlay for states that the person has traveled to.
    Color will be used in style function for fill.
    Adds overlay to map.
    """
    folium.GeoJson(data=state_geo,
                   name=person['Name'] + ' - '
                   + str(len(person['States'])),
                   style_function=state_style(person, color)
                   ).add_to(us_map)


'''
EXAMPLE CODE:

person_1 = {
    'Name' : 'Person 1',
    'States' : ['ME', 'FL', 'CA', 'WA', 'OR']
}

states_traveled(person_1, 'red')
'''

folium.LayerControl(hideSingleBase=True).add_to(us_map)
us_map.save('us_map.html')
