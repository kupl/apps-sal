from collections import defaultdict
from itertools import combinations


def lineEq(x, a, y, b):
    slope = (b - a) / (y - x)
    ordo = a - slope * x
    return ((slope, ordo), not slope % 1)


def fix_progression(arr):
    c = defaultdict(set)
    for ((x, a), (y, b)) in combinations(enumerate(arr), 2):
        (tup, isIntSlope) = lineEq(x, a, y, b)
        if isIntSlope:
            c[tup] |= {x, y}
    return len(arr) - max(map(len, c.values()))
