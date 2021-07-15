from itertools import *
from math import sqrt

def area_triang(a, b, c):
    s = (a + b + c)/2
    return sqrt(s * (s - a) * (s - b) * (s - c))

def calc_area(triangle):
    A, B, C = triangle
    c = sqrt(distance_sq(A, B))
    b = sqrt(distance_sq(A, C))
    a = sqrt(distance_sq(B, C))
    return area_triang(a, b, c)

def distance_sq(point1, point2):
    x1, y1, z1, = point1
    x2, y2, z2 = point2
    return (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2

def combin(point_list,i):
    return combinations(point_list, i)

def is_point_in_sphere(vert, center, r):
    dd = distance_sq(vert, center)
    return dd - r**2 < 0 and abs((sqrt(dd) - r) / r) > pow(10, -10)

def to_tup(point_list):
    point_list_ = []
    for point in point_list:
        point_list_.append(tuple(point))
    return point_list_

def triang_to_list(triang):
    pointA, pointB, pointC = triang
    return [list(pointA), list(pointB), list(pointC)]

def triangs_tolist(triang_list):
    res = []
    for triang in triang_list:
        res.append(triang_to_list(triang))
    return res

def biggest_triang_int(point_list, center, radius):
    point_list_ = []
    for point in point_list:
        if not is_point_in_sphere(point, center, radius): continue
        point_list_.append(point)
    point_list_ = to_tup(point_list_)
    triangs_area = {}
    for comb in combin(point_list_, 3):
        triangle  = tuple(comb)
        area = calc_area(triangle)
        if area < pow(10, -8): continue
        triangs_area[triangle] = area
    num_triangs = len(triangs_area)
    if num_triangs == 0: return []
    max_area = max(triangs_area.values())
    res = [num_triangs, max_area]
    sol = []
    for triang, area in triangs_area.items():
        if abs((area - max_area) / area) < pow(10, -10):
            sol.append(list(triang))
    if len(sol) == 1:
        sol_one = triang_to_list(sol[0])
        res.append(sol_one)
        return res
    else:
        sol_plus = triangs_tolist(sol)
        res.append(sol_plus)
    sol_plus.sort()
    return res
