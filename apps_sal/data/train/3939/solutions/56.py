def winner(a, b):
    return {'scissors': 'paper', 'rock': 'scissors', 'paper': 'rock'}[a] == b


def rps(p1, p2):
    return 'Draw!' if p1 == p2 else 'Player 1 won!' if winner(p1, p2) else 'Player 2 won!'
