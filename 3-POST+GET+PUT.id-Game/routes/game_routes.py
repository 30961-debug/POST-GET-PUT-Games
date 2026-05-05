from flask import Blueprint, request, jsonify
from controllers.game_controller import create_game, list_games, get_game, update_game_by_id

game_routes = Blueprint("game_routes", __name__)

@game_routes.route("/games", methods=["POST"])
def add_game_route():
    data = request.json
    new_game = create_game(data)
    return jsonify(new_game), 201

@game_routes.route("/games", methods=["GET"])
def list_games_route():
    return jsonify(list_games()), 200

@game_routes.route("/games/<int:id>", methods=["GET"])
def get_game_route(id):
    response, status = get_game(id)
    return jsonify(response), status

@game_routes.route("/games/<int:id>", methods=["PUT"])
def update_game_route(id):
    data = request.json
    response, status = update_game_by_id(id, data)
    return jsonify(response), status