def points(games):
    return sum([0, 1, 3][1 + (g[0] > g[2]) - (g[0] < g[2])] for g in games)
