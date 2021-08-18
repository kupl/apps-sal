from itertools import combinations
from math import hypot


def peaceful_yard(yard, min_distance):
    l, yard = len(yard[0]), "".join(yard)
    cats = (divmod(yard.index(c), l) for c in "LMR" if c in yard)
    distances = (hypot(x2 - x1, y2 - y1) for (x1, y1), (x2, y2) in combinations(cats, 2))
    return all(min_distance <= d for d in distances)
