from itertools import combinations
from math import hypot

def peaceful_yard(yard, min_distance):
    cats = [
        (r, c)
        for r, row in enumerate(yard)
        for c, x in enumerate(row)
        if x != '-'
    ]
    return all(
        hypot(a-c, b-d) >= min_distance
        for (a, b), (c, d) in combinations(cats, 2)
    )
