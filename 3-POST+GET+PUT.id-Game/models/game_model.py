games = [
    {"id": 1, "titulo": "Geometry Dash", "genero": "Rhythm", "desenvolvedor": "RobTop", "plataforma": "Pc"},
    {"id": 2, "titulo": "ULTRAKILL", "genero": "FPS", "desenvolvedor": "Arsi \"Hakita\" Patala", "plataforma": "PC"},
    {"id": 3, "titulo": "Hollow Knight", "genero": "Metroidvania", "desenvolvedor": "Team Cherry", "plataforma": "PS5"},
    {"id": 4, "titulo": "Hollow Knight: Silksong", "genero": "Metroidvania", "desenvolvedor": "Team Cherry", "plataforma": "PC"},
    {"id": 5, "titulo": "Deltarune", "genero": "RPG", "desenvolvedor": "Toby Fox", "plataforma": "PS5"}
]

def add_game(game):
    games.append(game)
    return game

def get_all_games():
    return games

def get_game_by_id(game_id):
    for game in games:
        if game["id"] == game_id:
            return game
    return None

def update_game(game_id, new_data):
    game = get_game_by_id(game_id)
    if game:
        game.update(new_data)
        return game
    return None