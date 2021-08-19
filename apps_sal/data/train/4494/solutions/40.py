def points(games):
    return sum([3 if x > y else 1 if x == y else 0 for (x, y) in (a.split(':') for a in games)])
