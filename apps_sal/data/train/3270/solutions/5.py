import itertools
squares = {i * i for i in range(1, 2000 + 1)}


def closest_pair_tonum(upper_lim):
    return next(((a, b) for (a, b) in itertools.combinations(range(upper_lim - 1, 0, -1), 2) if a + b in squares and a - b in squares))
