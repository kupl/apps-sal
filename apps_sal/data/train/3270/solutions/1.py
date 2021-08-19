from itertools import combinations


def closest_pair_tonum(upper_lim):
    return next(((x, y) for (x, y) in combinations(range(upper_lim - 1, 0, -1), 2) if ((x + y) ** 0.5).is_integer() and ((x - y) ** 0.5).is_integer()))
