rps = lambda p1, p2, l=["rock","paper","scissors"]: 'Draw!' if p1==p2 else 'Player {} won!'.format(1 + (l.index(p2)-l.index(p1) in [1,-2]))
