"""
travel.py - want to create a world map image with countries that I have traveled to, that J has traveled to, and that we have traveled to together. Also want to do the same with U.S. states.
"""

# import libraries
import folium

"""
TODO:
Add title to map. 
Change GeoJsons to not show all upon opening
See if file can be saved other than html
"""

"""
load the U.S. states json from folium repo, test folder
(w/added Washington DC)
"""

state_geo = 'C:/Users/Daniel/python_projects/travel/us-states.json'

dc = {'Name' : 'DC',
      'States' : ['VA', 'NC', 'SC', 'GA', 'FL', 'AL', 'WV', 'DC',
                  'PA', 'MD', 'DE', 'NJ', 'NY', 'MA', 'NH', 'ME','LA', 'OH', 'IN', 'MI', 'IL', 'WI', 'IA', 'MN',
                  'CO', 'NV', 'CA'
                 ],
      'Countries' : ['United States of America', 'Ireland',
                     'Netherlands', 'Belgium', 'France',
                     'Denmark', 'Spain', 'Switzerland', 'Germany','Costa Rica', 'Cayman Islands', 'Honduras','Belize', 'Mexico'
                    ]
     }

j = {'Name' : 'Julia',
     'States' : ['MA', 'NH', 'VT', 'RI', 'CT', 'NY', 'PA', 'NJ',
                 'MD', 'DE', 'WV', 'VA', 'NC', 'SC', 'GA', 'FL','MS', 'LA', 'TX', 'MI', 'MN', 'IL', 'CA', 'HI',
                 'DC'
                ],
     'Countries' : ['United States of America', 'Canada',
                    'Mexico', 'Cayman Islands', 'Honduras','Belize', 'Aruba', 'Puerto Rico',
                    'Costa Rica', 'Chile','Argentina', 'Spain','Portugal', 'Morocco', 'Italy', 'France'
                   ]
    }

camille = {'Name' : 'Camille',
           'States' : ['ME', 'VT', 'NH', 'RI', 'CT', 'NY', 'PA',
                       'MD', 'WV', 'NC', 'FL', 'LA', 'TX', 'CA',
                       'HI', 'DC', 'NJ', 'DE', 'MA', 'VA'
                      ]
          }

debbie = {'Name' : 'Debbie',
          'States' : ['TN', 'VA', 'OH', 'DC', 'NY', 'PA', 'NC',
                      'SC', 'MD', 'WV', 'FL', 'GA'
                     ]
         }

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
    Take a person's name and a color to create GeoJson overlay for states that the person has traveled to. Color will be used in style function for fill.
    """
    return folium.GeoJson(data=state_geo,
                          name=person['Name'] + ' - '
                              + str(len(person['States'])),
                          style_function=state_style(person, color)
                         )

states_traveled(dc, 'green').add_to(us_map)
states_traveled(j, 'blue').add_to(us_map)
states_traveled(camille, 'purple').add_to(us_map)
states_traveled(debbie, 'brown').add_to(us_map)

folium.LayerControl(hideSingleBase=True).add_to(us_map)
us_map.save('us_map.html')