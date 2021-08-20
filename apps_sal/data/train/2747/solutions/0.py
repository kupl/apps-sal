from itertools import combinations


def isRect(a, b, c):
    (X, Y, Z) = sorted((sum(((q - p) ** 2 for (p, q) in zip(p1, p2))) for (p1, p2) in [(a, b), (a, c), (b, c)]))
    return X + Y == Z


def count_rect_triang(points):
    return sum((isRect(*c) for c in combinations(set(map(tuple, points)), 3)))
