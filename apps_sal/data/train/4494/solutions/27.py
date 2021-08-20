def points(games):
    return sum((3 if x[0] > x[2] else 0 if x[0] < x[2] else 1 for x in games))
