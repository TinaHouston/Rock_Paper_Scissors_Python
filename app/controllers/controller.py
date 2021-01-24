from app import app
from flask import render_template
from app.models.player import *
from app.models.game import *

@app.route('/play')
def home():
    choice = ["rock", "paper", "scissors"]
    player_1 = Player("Player 1", choice)
    player_2 = Player("Player 2", choice)
    players = [player_1, player_2]
    return render_template('play.html', players=players)

@app.route('/<player_1_choice>')
def choice1(player_1_choice):
    return "Player 2, please type your choice into the browser after player 1's choice"

@app.route('/<player_1_choice>/<player_2_choice>')
def winner(player_1_choice, player_2_choice):
    winner = get_winner(player_1_choice, player_2_choice)
    winner_choice = show_winner_choice(player_1_choice, player_2_choice)
    return render_template("game.html", winner=winner, player_1_choice=player_1_choice, player_2_choice=player_2_choice, winner_choice=winner_choice)
