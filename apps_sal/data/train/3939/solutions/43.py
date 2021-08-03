def rps(p1, p2):
    v = {'p': 1, 'r': 0, 's': -1}
    return 'Draw!' if p1 == p2 else 'Player 1 won!' if v[p1[0]] - v[p2[0]] in [1, -2] else 'Player 2 won!'
