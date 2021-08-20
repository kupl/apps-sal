def rps(p1, p2):
    winner = {'scissors': 'paper', 'paper': 'rock', 'rock': 'scissors'}
    if p1 == p2:
        return 'Draw!'
    elif winner[p1] == p2:
        return 'Player 1 won!'
    elif winner[p2] == p1:
        return 'Player 2 won!'
