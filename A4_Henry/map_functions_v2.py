"""
Published: June 25, 2023

The map_functions script showcases functions that will be evaluated and applied to the final project, specifically for map visualization and user input.

The included functions can perform the following:
1. Create Map - Map creation with user-defined inputs
2. Draw Polygon - Allow the user to draw a polygon on the map to be used in further analysis
3. Add Shapefile to Map - Allow the user to add a shapefile to the map to be used for further analysis.
"""

import geopandas as gpd
import folium
from folium.plugins import Draw
import ipywidgets as widgets
from IPython.display import display

#Function 1 - Create Map

def create_custom_map():
    """
    Creates a new map with user-defined coordinates and zoom level.

    Args:
        latitude (float): Latitude of the map center.
        longitude (float): Longitude of the map center.
        zoom (int): Zoom level of the map.

    Returns:
        folium.Map: Custom map object.
    """
    # Create input widgets for latitude, longitude, and zoom level
    latitude_input = widgets.FloatText(description='Latitude:')
    longitude_input = widgets.FloatText(description='Longitude:')
    zoom_input = widgets.IntText(description='Zoom Level:')
    
    # Display the input widgets
    display(latitude_input, longitude_input, zoom_input)
    
    # Wait for the user to enter the inputs
    widgets.interact_manual.options(manual_name="Create Map")
    widgets.interact_manual(create_map, latitude=latitude_input, longitude=longitude_input, zoom_level=zoom_input)
    
def create_map(latitude, longitude, zoom_level):
    # Create a Folium map centered around the specified coordinates
    custom_map = folium.Map(location=[latitude, longitude], zoom_start=zoom_level)
    
    # Display the map
    display(custom_map)






