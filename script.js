const fs = require('fs');

// Load the mapData from the map.js file
let mapData = require('./map.js');

// Find the item you want to update
let item = mapData.find(d => d.id === 'id0');

// Update the item
item.type = 'NEW_TYPE';
item.continent = 'NEW_CONTINENT';
item.controller = 'NEW_CONTROLLER';
item.name = 'NEW_NAME';

// Save the updated mapData back to the map.js file
fs.writeFileSync('./map.js', 'var mapData = ' + JSON.stringify(mapData, null, 2) + ';');
