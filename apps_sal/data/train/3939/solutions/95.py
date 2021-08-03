DRAW = 'Draw!'
P1_WIN = 'Player 1 won!'
P2_WIN = 'Player 2 won!'
gamestate = {
    'rock': {'rock': DRAW, 'paper': P2_WIN, 'scissors': P1_WIN, },
    'paper': {'rock': P1_WIN, 'paper': DRAW, 'scissors': P2_WIN, },
    'scissors': {'rock': P2_WIN, 'paper': P1_WIN, 'scissors': DRAW, }
}


def rps(p1, p2):
    return gamestate[p1][p2]


def rps2(p1, p2):
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    elif p1 == p2:
        return "Draw!"
    elif p1 == "paper" and p2 == "scissors":
        return "Player 2 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
