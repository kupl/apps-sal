def rps(p1, p2):
    d = dict(rock=0, paper=1, scissors=2)
    return ('Draw!', 'Player 1 won!', 'Player 2 won!')[(d[p1] - d[p2]) % 3]
