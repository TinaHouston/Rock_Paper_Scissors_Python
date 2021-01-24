from app.models.player import Player

class Game:
    pass

def get_winner(player_1_choice, player_2_choice):
    winner = None

    if player_1_choice == player_2_choice:
        winner = None
    if player_1_choice == "rock" and player_2_choice == "scissors":
        winner = "Player 1"
    if player_1_choice == "scissors" and player_2_choice == "paper":
        winner = "Player 1"
    if player_1_choice == "paper" and player_2_choice == "rock":
        winner = "Player 1"
    if player_2_choice == player_1_choice:
        winner = None
    if player_2_choice == "rock" and player_1_choice == "scissors":
        winner = "Player 2"
    if player_2_choice == "scissors" and player_1_choice == "paper":
        winner = "Player 2"
    if player_2_choice == "paper" and player_1_choice == "rock":
        winner = "Player 2"

    return winner

def show_winner_choice(player_1_choice, player_2_choice):
    winner_choice = None

    if player_1_choice == "rock" and player_2_choice == "scissors":
        winner_choice = "rock"
    if player_1_choice == "scissors" and player_2_choice == "paper":
        winner_choice = "scissors"
    if player_1_choice == "paper" and player_2_choice == "rock":
        winner_choice = "paper"
    if player_2_choice == "rock" and player_1_choice == "scissors":
        winner_choice = "rock"
    if player_2_choice == "scissors" and player_1_choice == "paper":
        winner_choice = "scissors"
    if player_2_choice == "paper" and player_1_choice == "rock":
        winner_choice = "paper"

    return winner_choice