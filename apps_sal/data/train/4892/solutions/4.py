from itertools import combinations


def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5


def triangle_area(A, B, C):
    a, b, c = sorted([dist(A, B), dist(A, C), dist(B, C)])
    if a + b > c and c - a < b:
        s = round(((a + b + c) * (a + b - c) * (a + c - b) * (b + c - a))**0.5 / 4, 1)
    else:
        s = None
    return s


def find_biggTriang(listPoints):
    num_points = len(listPoints)
    possible_count = 0
    real_count = 0
    areas = {}
    max_area = 0
    for x in combinations(listPoints, 3):
        possible_count += 1
        area = triangle_area(*x)
        if area:
            areas[x] = area
            max_area = max(max_area, area)
            real_count += 1
    max_triangles = [list(map(list, k))
                     for k, v in list(areas.items()) if v == max_area]
    if len(max_triangles) == 1:
        max_triangles = max_triangles[0]
    return [num_points, possible_count, real_count, max_triangles, max_area]
