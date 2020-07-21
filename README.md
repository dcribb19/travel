# travel
Create a personal overlay on a map of the U.S. of states that you have traveled to with a custom color.

## Motivation
The purpose of this project is to be able to visualize the states that you have traveled to and to be able to compare your travels with those of anyone else. 

## Examples
![text](https://github.com/dcribb19/travel/blob/master/examples/travel_1.png '1 Person')  
![text](https://github.com/dcribb19/travel/blob/master/examples/travel_2.png 'Comparing 2 People')  

## Technology
- Python 3.8
- folium 0.11.0

## Usage
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

## Credits
[folium](https://python-visualization.github.io/folium/)

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)