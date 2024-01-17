import pprint
import json
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from currancy import JamesCurrancyAPI, RunAPI
#from ext import ShopAPI, Shop
from scoreboard import ScoreBoard

app = Flask(__name__)
CORS(app)
@app.post("/v1/chat/rewards")
def rewards():
    payload = request.json
    api = RunAPI()
    return jsonify(api.rewards(payload=payload))

@app.post("/v1/chat/items")
def items():
    payload = request.json
    api = RunAPI()
    return jsonify(api.item(payload=payload))

@app.post("/v1/chat/gamewin")
def game_win():
    payload = request.json
    api = RunAPI()
    return jsonify(api.game_win(payload))

@app.post("/v1/get/items")
def get_items():
    payload = request.json
    username = payload['name']
    api = RunAPI()
    return jsonify(api.get_items(username=username))

@app.post("/v1/get/currency")
def get_currency():
    payload = request.json
    api = RunAPI()
    return jsonify(api.get_currancy(payload))

#@app.post("/newiteminshop")
#def add_item_in_shop():
    #payload = request.json
    #api = Shop()
    #return jsonify(api.items(payload))

@app.post("/v1/get/scoreboard")
def scoreboard():
    payload = request.json
    game = payload['game']
    api = ScoreBoard()
    return jsonify(api.get_players(game=game))

def scoreboard_internal(game):
    payload = request.json
    api = ScoreBoard()
    return api.get_players(game=game)

@app.post("/v1/chat/bot/scoreboard")
def bot():
    payload = request.json
    print(payload)
    game = payload['text'].split()[2]
    print(game)
    scoreboard_s = scoreboard_internal(game)
    scoreboard_s = dict(sorted(scoreboard_s.items(), key=lambda item: item[1], reverse=True))
    print(scoreboard_s)
    html = "<ol>"
    for item in scoreboard_s:
        print(item)
        html += "<li>" + item + "</li>"
    html += "</ol>"
    return jsonify({"author": "Manager", "text": html})

@app.post("/v1/chat/bot/currency")
def bot_currency():
    payload = request.json
    
    currency = get_currency_internal(payload=payload)
    message = f"You have {currency['currancy']} JCR"
    return jsonify({"author": "Manager", "text": message})

def get_currency_internal(payload):
    
    api = RunAPI()
    return api.get_currancy(payload)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
