# travel
Create a personal overlay on a map of the U.S. of states that you have visited or on a map of the world of countries that you have visited with a custom color.

## Motivation
The purpose of this project is to be able to visualize the U.S. states that you have traveled to or countries that you have traveled to. Additionally, you are able to compare your travels with those of anyone else with multiple overlays on the same map.

## Examples
![text](https://github.com/dcribb19/travel/blob/master/examples/travel_1.png '1 Person')  
![text](https://github.com/dcribb19/travel/blob/master/examples/travel_2.png 'Comparing 2 People')
![text](https://github.com/dcribb19/travel/blob/master/examples/world.png '2 People World')

## Technology
- Python 3.8
- folium 0.11.0

## Usage
### For U.S. states
- In travel_folium.py, create a dictionary with the following structure for each person:
    - Value of 'States' should be a list of strings of state abbreviations, such as: ['AL', 'AK', 'CA', 'WA']
    ```python
    person = {
        'Name' : 'person_name',
        'States' : []
    }
    ```
- For each person, call the states_traveled function passing the person dictionary and a color string for the fill color you prefer. 
    ```python
    states_traveled(person: dict, color: str)
    ```
- us-states.json is used to create the overlay.
- Legend provides total number of states traveled to and allows for selection to compare different people.  
    ![text](https://github.com/dcribb19/travel/blob/master/examples/legend.png 'Legend')
- File will be saved as us_map.html.

### For Countries
- In world_travel.py, create a dictionary with the following structure for each person:
    - Value of 'Countries' should be a list of strings of country names, such as: ['Peru', 'Chile', 'United States of America', 'Sweden']
    ```python
    person = {
        'Name' : 'person_name',
        'Countries' : []
    }
    ```
- For each person, call the countries_traveled function passing the person dictionary and a color string for the fill color you prefer. 
    ```python
    countries_traveled(person: dict, color: str)
    ```
- world-countries.json is used to create the overlay.
- Legend provides total number of countries traveled to and allows for selection to compare different people.  
- File will be saved as world_map.html.

## Credits
[folium](https://python-visualization.github.io/folium/)

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)