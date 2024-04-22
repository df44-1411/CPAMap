import re
import json

# Read map data from JavaScript file
with open('map_data.js', 'r') as file:
    js_content = file.read()

# Extract mapData from JavaScript content using regex
map_data_match = re.search(r'mapData:\s*(\[.*?\])', js_content, re.DOTALL)
if map_data_match:
    map_data_js = map_data_match.group(1)
    # Convert JavaScript array to Python list
    map_data = eval(map_data_js)

    # Count occurrences of each controller
    controller_counts = {}
    for entry in map_data:
        controller = entry.get('controller')
        if controller:
            controller_counts[controller] = controller_counts.get(controller, 0) + 1

    # Read colors from CSS file
    with open('styles.css', 'r') as css_file:
        css_content = css_file.read()

    # Extract color for each controller
    controller_colors = {}
    for controller in controller_counts.keys():
        color_match = re.search(f'\.{controller}\s*{{.*?color\s*:\s*(.*?);', css_content, re.DOTALL)
        if color_match:
            color = color_match.group(1).strip()
            controller_colors[controller] = color

    # Generate HTML content
    html_content = "<!DOCTYPE html>\n<html>\n<head>\n<title>Controller Counts</title>\n<style>\n"
    for controller, count in controller_counts.items():
        color = controller_colors.get(controller, '#000000')  # Default to black if color not found
        html_content += f".{controller} {{ color: {color}; font-weight: bold; }}\n"
    html_content += "</style>\n</head>\n<body>\n"
    html_content += "<h1>Controller Counts</h1>\n<ul>\n"
    for controller, count in controller_counts.items():
        html_content += f"<li><span class='{controller}'>{controller} ({count})</span></li>\n"
    html_content += "</ul>\n</body>\n</html>"

    # Write HTML content to file
    with open('controller_counts.html', 'w') as file:
        file.write(html_content)

    print("HTML file created successfully!")
else:
    print("Failed to find mapData in the JavaScript file.")
