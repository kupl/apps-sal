def rps(p1, p2):
    rule = {'scissors': 'paper', 'paper': 'rock', 'rock': 'scissors'}
    return ['Player %d won!' % [2, 1][rule[p1] == p2], 'Draw!'][p1 == p2]
