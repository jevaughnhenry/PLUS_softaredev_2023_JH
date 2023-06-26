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

#Function 1 - Create Map
def create_new_map():
    """
    Creates a new map with user-defined coordinates and zoom level.

    Args:
        latitude (float): Latitude of the map center.
        longitude (float): Longitude of the map center.
        zoom (int): Zoom level of the map.

    Returns:
        folium.Map: Custom map object.
    """
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))
    zoom = int(input("Enter zoom level: "))

    new_map = folium.Map(location=[latitude, longitude], zoom_start=zoom)
    return new_map

# Create a new custom map
new_map = create_new_map()

# Display the map
new_map


#Function 2 - Draw Polygon
def add_draw_control(m):
    """
    Adds a draw control to the user-defined map to allow the drawing of polygons for further analysis.
    
    Returns:
        folium.Map: User-defined map object with the polygon drawing control.
    """

    # Add the draw control to the map
    draw = Draw(export=True)
    draw.add_to(m)

    # Return the map object with the draw control
    return m

# Add existing map object from user-defined map
m = new_map

# Call the function to add the draw control to the map
map_with_draw_control = add_draw_control(m)

# Display the map with the draw control
map_with_draw_control

#Function 3 - Add Shapefile to Map
def add_shapefile_to_map(m):
    """
    Allows the user to add a shapefile to the map to be used for further analysis.

    Args:
        shapefile_path (gpd): Path to a shapefile to be displayed on the map.
        m (folium.Map): Map object with the shapefile will be added.
        
    Returns:
        folium.Map: Previously created custom map object with the desired shapefile added.
    """
    
    # Allow the user to enter the path to the shapefile
    shapefile_path = input("Enter the path to the shapefile: ")

    # Read the shapefile into a GeoDataFrame
    gdf = gpd.read_file(shapefile_path)

    # Convert the GeoDataFrame to GeoJSON format
    geojson_data = gdf.to_crs('EPSG:4326').to_json()

    # Create a Folium GeoJson object and add it to the map
    folium.GeoJson(geojson_data).add_to(m)

    # Return the updated map
    return m

# Create a Folium map
m = new_map

# Call the function to add the shapefile to the map
new_map = add_shapefile_to_map(m)

# Display the map
new_map