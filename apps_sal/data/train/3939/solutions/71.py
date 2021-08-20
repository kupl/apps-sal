def rps(p1, p2):
    pairs = {'scissors': 'paper', 'paper': 'rock', 'rock': 'scissors'}
    if pairs[p1] == p2:
        return 'Player 1 won!'
    elif pairs[p2] == p1:
        return 'Player 2 won!'
    else:
        return 'Draw!'
