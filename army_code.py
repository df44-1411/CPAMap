# Define the sentences to search for and their corresponding colors
search_terms = {
    "Club Penguin Armies": "#87d1ff",
    "CPA Battleground": "#dd2100",
    "Club Penguin Army Judges": "#ca2244",
    "Water Vikings": "#000080",
    "Army of Club Penguin": "#008000",
    "Elite Guardians of Club Penguin": "grey",
    "Special Weapons and Tactics": "#00ff00",
    "Silver Empire": "white",
    "People's Imperial Confederation": "#333399",
    "Dark Pirates": "#800000",
    "Templars": "#ffcc00",
    "Rebel Penguin Federation": "#000000",
    "Winged Hussars": "#ff0000",
    "Help Force": "#0000ff",
    "Smart Penguins": "red",
    "Warlords of Kosmos": "black",
    "Freeland" : "grey"
}

# Open the file in read mode
with open('map.js', 'r') as file:
    # Read the content of the file
    content = file.read()

# Initialize the HTML content
html_content = "<html><body style='font-family: sans-serif;'>"

# Iterate over the search terms
for term, color in search_terms.items():
    # Count the occurrences of the term in the content
    count = content.lower().count(term.lower()) - 1

    # If the term appears more than once
    if count >= 1:
        # Add a line to the HTML content
        html_content += f'<p style="color: {color}; font-weight: bold;">{term} ({count})</p>'

# Close the HTML tags
html_content += "</body></html>"

# Write the HTML content to "army_code.html"
with open("army_code.html", 'w') as file:
    file.write(html_content)
