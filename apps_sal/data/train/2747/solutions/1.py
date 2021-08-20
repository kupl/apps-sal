from itertools import combinations


def count_rect_triang(points):
    result = 0
    for ((x1, y1), (x2, y2), (x3, y3)) in combinations(set(map(tuple, points)), 3):
        d1 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        d2 = (x2 - x3) ** 2 + (y2 - y3) ** 2
        d3 = (x3 - x1) ** 2 + (y3 - y1) ** 2
        (d1, d2, d3) = sorted((d1, d2, d3))
        result += d1 + d2 == d3
    return result
