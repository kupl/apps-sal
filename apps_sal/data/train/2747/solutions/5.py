from itertools import product


def count_rect_triang(points):
    return sum(1
               for p0, p1, p2 in product(set(map(tuple, points)), repeat=3)
               if p0 != p1 != p2 != p0 and (p1[0] - p0[0]) * (p2[0] - p0[0]) + (p1[1] - p0[1]) * (p2[1] - p0[1]) == 0
               ) // 2
