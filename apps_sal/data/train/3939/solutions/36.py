def rps(p1, p2):
    rule = {'scissors': 'paper', 'paper': 'rock', 'rock': 'scissors'}
    if p1 == p2:
        return 'Draw!'
    elif rule[p1] == p2:
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
