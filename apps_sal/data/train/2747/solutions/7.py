from itertools import combinations


def count_rect_triang(points):
    n = 0
    points_set = set()
    for p in points:
        points_set.add(tuple(p))
    for (x1, y1), (x2, y2), (x3, y3) in combinations(points_set, 3):
        l1, l2, l3 = sorted([(x2 - x1)**2 + (y2 - y1)**2, (x3 - x2)**2 + (y3 - y2)**2, (x1 - x3)**2 + (y1 - y3)**2])
        if l1 + l2 == l3:
            n += 1
    return n
