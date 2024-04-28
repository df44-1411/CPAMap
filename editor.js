function fetchData() {
    var idOrName = $('#idInput').val();
    var data = mapData.find(d => d.id === idOrName || d.name === idOrName);
    if (data) {
        $('#dataContainer').html(`
            <input id="typeInput" value="${data.type}">
            <input id="continentInput" value="${data.continent}">
            <input id="controllerInput" value="${data.controller}">
            <input id="nameInput" value="${data.name}">
            <button onclick="saveData('${data.id}')">Save</button>
        `);
    } else {
        $('#dataContainer').html('No data found for that ID or name.');
    }
}

function saveData(id) {
    var data = mapData.find(d => d.id === id);
    if (data) {
        data.type = $('#typeInput').val();
        data.continent = $('#continentInput').val();
        data.controller = $('#controllerInput').val();
        data.name = $('#nameInput').val();
        // Add changes to github
        commitChangesToGithub();
    }
}

function commitChangesToGithub() {
    //To be coded
}
