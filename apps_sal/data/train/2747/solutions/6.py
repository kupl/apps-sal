from itertools import combinations


def dist(ps):
    p1, p2, p3 = ps
    x = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    y = (p1[0] - p3[0])**2 + (p1[1] - p3[1])**2
    z = (p2[0] - p3[0])**2 + (p2[1] - p3[1])**2
    return sorted([x, y, z])


def count_rect_triang(points):
    if len(points) < 3:
        return 0
    ps = []
    for i in points:
        if i not in ps:
            ps.append(i)
    c = 0
    for i in combinations(ps, 3):
        temp = dist(i)
        if round(temp[-1], 4) == round(temp[0] + temp[1], 4):
            c += 1
    return c
