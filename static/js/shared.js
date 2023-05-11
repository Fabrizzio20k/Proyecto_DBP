function list_games(games) {
    const container_games = document.getElementByClassName("container_games")[0]
    if (games.length == 0) {
        container_games.innerHTML = "There are no games"
    } else {
        container_games.innerHTML = ""
        games.forEach((game) => {
            const block = document.createElement("div")
            classs.add("item_game")

            block.innerHTML = `
                    <img src="${game.image}">
                    <h2>${game.game_name}</h4>
                    <p>${game.synopsis}</div>
                    `
            container_games.appendChild(block)
        })
    }
}

function update_search_params(categoria, elemento) {
    let url = new URL(window.location)
    url.searchParams.set(categoria, elemento)

    url.search = url.searchParams
    url = url.toString()

    history.pushState({}, null, url)

    fetch(`/do_search`)
        .then(function (response) {
            return response.json()
        }).then(function (jsonResponse) {
            const games = jsonResponse.games
            list_games(games)
        })
}
