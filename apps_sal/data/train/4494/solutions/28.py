def points(games):
    diff = map(lambda x: int(x[0]) - int(x[-1]), games)
    wins = map(lambda x: 3 if x > 0 else x, diff)
    return sum(list(map(lambda x: 1 if x == 0 else x * (x > 0), wins)))
