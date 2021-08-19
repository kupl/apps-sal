from itertools import combinations
from math import sqrt


# determinant of matrix a
def det(a):
    return a[0][0] * a[1][1] * a[2][2] + \
        a[0][1] * a[1][2] * a[2][0] + \
        a[0][2] * a[1][0] * a[2][1] - \
        a[0][2] * a[1][1] * a[2][0] - \
        a[0][1] * a[1][0] * a[2][2] - \
        a[0][0] * a[1][2] * a[2][1]


# unit normal vector of plane defined by points a, b, and c
def unit_normal(a, b, c):
    x = det([[1, a[1], a[2]],
             [1, b[1], b[2]],
             [1, c[1], c[2]]])
    y = det([[a[0], 1, a[2]],
             [b[0], 1, b[2]],
             [c[0], 1, c[2]]])
    z = det([[a[0], a[1], 1],
             [b[0], b[1], 1],
             [c[0], c[1], 1]])
    magnitude = (x**2 + y**2 + z**2)**.5
    return x / magnitude, y / magnitude, z / magnitude


# dot product of vectors a and b
def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


# cross product of vectors a and b
def cross(a, b):
    x = a[1] * b[2] - a[2] * b[1]
    y = a[2] * b[0] - a[0] * b[2]
    z = a[0] * b[1] - a[1] * b[0]
    return x, y, z


# area of polygon poly
def area(poly):
    if len(poly) < 3:  # not a plane - no area
        return 0

    total = [0, 0, 0]
    for i in range(len(poly)):
        vi1 = poly[i]
        if i is len(poly) - 1:
            vi2 = poly[0]
        else:
            vi2 = poly[i + 1]
        prod = cross(vi1, vi2)
        total[0] += prod[0]
        total[1] += prod[1]
        total[2] += prod[2]
    result = dot(total, unit_normal(poly[0], poly[1], poly[2]))
    return [abs(result / 2), poly]


def distance(a, b):
    pow_each = [pow(x, 2) for x in map(lambda x, y: x - y, a, b)]
    sum_all = sum(pow_each)
    return sqrt(sum_all)


def out_side(point, c, r):
    return distance(point, c) <= r


def all_max(elements, key):
    if not elements:
        return 0, []
    value = max(elements, key=key)[0]
    results = [j for i, j in elements if i == value]
    return value, results if len(results) > 1 else results[0]


def biggest_triang_int(point_list, center, radius):
    valid_points = [x for x in point_list if out_side(x, center, radius)]
    comb_elements = list(combinations(valid_points, 3))
    results = [area(x) for x in list(map(list, comb_elements))]
    result, poly = all_max(results, key=lambda x: x[0])
    return [len(comb_elements), result, poly] if results else []
