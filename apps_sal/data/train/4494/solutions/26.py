def points(games):
    return sum(((x >= y) * (1 + 2 * (x > y)) for (x, y) in map(lambda s: s.split(':'), games)))
