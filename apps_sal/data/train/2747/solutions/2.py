from itertools import combinations


def ok(a, b, c):
    ((x1, y1), (x2, y2), (x3, y3)) = (a, b, c)
    (d1, d2, d3) = ((x1 - x2) ** 2 + (y1 - y2) ** 2, (x1 - x3) ** 2 + (y1 - y3) ** 2, (x2 - x3) ** 2 + (y2 - y3) ** 2)
    (d1, d2, d3) = sorted([d1, d2, d3])
    return d1 + d2 == d3


def count_rect_triang(points):
    return sum((ok(pa, pb, pc) for (pa, pb, pc) in combinations(set(map(tuple, points)), 3)))
