from itertools import combinations


def area(t):
    ((a, b), (c, d), (e, f)) = t
    return abs(a * d + b * e + c * f - d * e - a * f - b * c) / 2


def find_biggTriang(lst):
    tris = list(combinations(lst, 3))
    areas = list(map(area, tris))
    m = max(areas)
    mTris = [list(map(list, t)) for (t, v) in zip(tris, areas) if v == m]
    return [len(lst), len(tris), sum(map(bool, areas)), mTris if len(mTris) != 1 else mTris.pop(), m]
