def rps(p1, p2):
    beat_dict = {'scissors': 'paper', 'paper': 'rock', 'rock': 'scissors'}
    return 'Draw!' if p1 == p2 else 'Player 1 won!' if beat_dict[p1] == p2 else 'Player 2 won!'
