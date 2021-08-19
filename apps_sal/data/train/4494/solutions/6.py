def points(g):
    return sum(((x > y) * 3 or x == y for (x, _, y) in g))
