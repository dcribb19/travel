# travel
Create overlays on U.S. map of states that you have traveled to.

## Motivation
The purpose of this project is to be able to visualize the states that you have traveled to and to be able to compare your travels with anyone else. 

## Examples
![text](https://github.com/dcribb19/travel/blob/master/examples/travel_1.png '1 Person')
![text](https://github.com/dcribb19/travel/blob/master/examples/travel_2.png 'Comparing 2 People')

## Technology
- Python 3.8

## Usage
- Install folium (if not already installed).
- Keep travel_folium.py and us-states.json in the same directory.
- Create a dictionary with the following structure for each person:
    - Value of 'states' should be a list of strings of state abbreviations.
```python
person = {
    'name' : 'person_name',
    'states' : []
}
```
- For each person, call the states_traveled function passing the person dictionary and a color string for the fill color you prefer. 
```python
states_traveled(person: dict, color: str)
```
- Legend provides total number of states traveled to and allows for selection to compare different people.
-- ![text](https://github.com/dcribb19/travel/blob/master/examples/legend.png 'Legend')
- File will be saved as us_map.html.

## Credits
- [folium](https://python-visualization.github.io/folium/)

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)