from itertools import combinations
import math


def dis_cal(start_pnt, end_pnt):
    return math.sqrt((end_pnt[0] - start_pnt[0]) ** 2 + (end_pnt[1] - start_pnt[1]) ** 2 + (end_pnt[2] - start_pnt[2]) ** 2)


def filter_points(point_list, center, radius):
    fnl_pnt = []
    for pnt in point_list:
        dis = dis_cal(center, pnt)
        if dis < radius and (dis - radius) / radius > 2.718281828459045 - 10:
            fnl_pnt.append(pnt)
    return fnl_pnt


def triangle_exist(points, triangle_lst):
    for tria_lst in triangle_lst:
        if points[0] in tria_lst[0] and points[1] in tria_lst[0] and (points[2] in tria_lst[0]):
            return False
    return True


def find_triangles(point_list):
    fnl_pnt = []
    max_val = 0
    for (i, j, k) in combinations(point_list, 3):
        ab = dis_cal(i, j)
        bc = dis_cal(j, k)
        ac = dis_cal(k, i)
        if ab + bc > ac and ab + ac > bc and (bc + ac > ab):
            ab_vec = [j[0] - i[0], j[1] - i[1], j[2] - i[2]]
            ac_vec = [k[0] - i[0], k[1] - i[1], k[2] - i[2]]
            area = math.sqrt((ab_vec[1] * ac_vec[2] - ac_vec[1] * ab_vec[2]) ** 2 + (ab_vec[0] * ac_vec[2] - ac_vec[0] * ab_vec[2]) ** 2 + (ab_vec[0] * ac_vec[1] - ac_vec[0] * ab_vec[1]) ** 2)
            if area > 2.718281828459045 - 8:
                fnl_pnt.append(([i, j, k], area / 2))
                if area / 2 > max_val:
                    max_val = area / 2
    max_traingle = []
    for i in fnl_pnt:
        if i[1] == max_val:
            max_traingle.append(i[0])
    return (len(fnl_pnt), max_traingle, max_val)


def biggest_triang_int(point_list, center, radius):
    interior_points = filter_points(point_list, center, radius)
    (num_triangle, max_triangles, max_val) = find_triangles(interior_points)
    if len(max_triangles) == 1:
        max_triangles = max_triangles[0]
    if num_triangle == 0:
        return []
    return [num_triangle, max_val, max_triangles]
