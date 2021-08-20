def points(games):
    return sum([3 if g[0] > g[-1] else 1 if g[0] == g[-1] else 0 for g in games])
