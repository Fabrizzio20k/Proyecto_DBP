function change_videogame() {
    fetch("/get_videogame").then(function (response) {
        return response.json()
    }).then(function (jsonResponse) {
        const game_platform = jsonResponse.game_platform
        const platform_game = game_platform.platform

        const platform = game_platform.platform
        const game_puplisher = game_platform.publisher
        const puplisher = game_publisher.publisher
        const game = game_publisher.game
        const genre_game = game.genre

        const title = document.getElementByTagName("title")[0]

        const game_name = document.getElementById("game_name")

        game_name.innerHTML = `${game.game_name}`

        const container_image = document.getElementById("game_image")
        container_image.innerHTML = `
                        <img src="${game.image}" alt="Game Image">
                        `

        const synopsis = document.getElementById("synopsis")
        synopsis.innerHTML = `Sinopsis: ${game.synopsis}`

        const year = document.getElementById("year")
        year.innerHTML = `Año de lanzamiento: ${game_platform.release_year}`

        const genre_tag = document.getElementById("genre")
        genre_tag.innerHTML = `Sinopsis: ${genre_tag.genre_name}`

        const publisher = document.getElementById("publisher")
        publisher.innerHTML = `Editor: ${publisher.publisher_name}`

        const platform_tag = document.getElementById("platform")
        platform_tag.innerHTML = `Plataforma: ${platform_tag.platform_name}`
    })
}

function comprar(event) {
    event.preventDefault();

    fetch("/is_game_bought").then(function (response) {
        return rsponse.json()
    }).then(function (jsonResponse) {
        if (jsonResponse.is_bought == 1) {
            const buy_message = document.getElementById("buy_message")
            buy_message.innerHTML = "Ya has comprado este juego"
        } else {
            fetch('/buy_game', {
                method: 'POST',
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success === true) {
                        window.location.href = '/checkout';
                    } else {
                        const buy_message = document.getElementById("buy_message")
                        buy_message.innerHTML = 'La verificación de compra no fue exitosa'
                    }
                })
                .catch(error => {
                    const buy_message = document.getElementById("buy_message")
                    buy_message.innerHTML = 'Error al realizar la verificación de compra:'
                });
        }
    })
}

window.onload = function() {
    change_videogame()
    change_buy_button()
}
