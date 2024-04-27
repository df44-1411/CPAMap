import json
import re

# Define a function to extract map data from the JavaScript file
def extract_map_data(js_file_path):
    # Read the JavaScript file
    with open(js_file_path, 'r') as file:
        js_content = file.read()

    # Find the map data in the JavaScript content
    map_data_match = re.search(r'mapData: (\[.*?\])', js_content, re.DOTALL)

    # If the map data is found
    if map_data_match:
        # Extract the map data as a JSON string
        map_data_json = map_data_match.group(1)

        # Parse the JSON string into a Python list
        map_data = json.loads(map_data_json)

        # Return the map data
        return map_data

    # If the map data is not found, return an empty list
    return []

# Call the function to extract map data from "map.js"
map_data = extract_map_data("map.js")

# Initialize a counter
freeland_count = 0

# Iterate over the map data
for data_point in map_data:
    # If the controller is 'Freeland', increment the counter
    if data_point["controller"].lower() == "freeland":
        freeland_count += 1

# Prepare the HTML content
html_content = f"<html><body><p>The controller 'Freeland' appears {freeland_count} times in the map data.</p></body></html>"

# Write the HTML content to "output.html"
with open("output.html", 'w') as file:
    file.write(html_content)
