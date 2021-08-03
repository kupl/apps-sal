def rps(p1, p2):
    d = {'scissors': 'paper', 'rock': 'scissors', 'paper': 'rock'}
    return 'Draw!' if p1 == p2 else 'Player 1 won!' if d[p1] == p2 else 'Player 2 won!'
