from math import hypot
from statistics import mean


def cluster(points, n):
    cs = [[p] for p in points]

    def key(ij):
        return mean(dist(p1, p2) for p1 in cs[ij[0]] for p2 in cs[ij[1]])
    while len(cs) > n:
        i, j = min(((i, j) for i in range(len(cs)) for j in range(i)), key=key)
        cs[i] += cs[j]
        del cs[j]
    return sorted(map(sorted, cs))


def dist(a, b):
    return hypot(a[0] - b[0], a[1] - b[1])
