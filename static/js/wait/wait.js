setTimeout(function() {
  let url = new URLSearchParams(document.location.search)
  let id_game = url.get("id")

  window.location.href = '/resume';
  update_search_params("id", id_game)
}, 5000);
