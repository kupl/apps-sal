from itertools import product, combinations
from math import hypot


def euclid(p):
    (x1, y1), (x2, y2) = p
    return hypot(x1 - x2, y1 - y2)


def sim(pc):
    pc1, pc2 = pc
    return sum(map(euclid, product(pc1, pc2))) / (len(pc1) * len(pc2))


def cluster(points, n):
    res = [[p] for p in points]
    while len(res) > n:
        p0, p1 = min(combinations(res, 2), key=sim)
        res.remove(p0)
        res.remove(p1)
        res.append(p0 + p1)
    return sorted(map(sorted, res))
