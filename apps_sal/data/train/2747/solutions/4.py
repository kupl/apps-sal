from itertools import combinations


def count_rect_triang(points):
    return sum((1 for ps in combinations(set(map(tuple, points)), 3) for (p0, p1, p2) in ((ps[0], ps[1], ps[2]), (ps[1], ps[2], ps[0]), (ps[2], ps[1], ps[0])) if (p1[0] - p0[0]) * (p2[0] - p0[0]) + (p1[1] - p0[1]) * (p2[1] - p0[1]) == 0))
