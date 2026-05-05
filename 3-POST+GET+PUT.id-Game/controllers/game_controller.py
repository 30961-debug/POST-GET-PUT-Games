from models.game_model import add_game, get_all_games, get_game_by_id, update_game

def create_game(data):
    return add_game(data)

def list_games():
    return get_all_games()

def get_game(id):
    game = get_game_by_id(id)
    if game:
        return game, 200
    return {"message": "Jogo não encontrado"}, 404

def update_game_by_id(id, data):
    game = update_game(id, data)
    if game:
        return game, 200
    return {"message": "Jogo não encontrado"}, 404