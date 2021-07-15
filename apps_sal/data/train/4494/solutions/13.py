def points(games):
    return sum(3*(x > y) + (x == y) for x, _, y in games)
