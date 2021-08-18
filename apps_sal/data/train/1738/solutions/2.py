from math import sqrt
from itertools import combinations


def sort_key(tri_list, tri):
    '''Returns an integer found by concatenating the indecies of the points in
    the triangle'''
    x, y, z = tri
    deg = len(str(len(tri_list)))
    x_dex, y_dex, z_dex = tri_list.index(x), tri_list.index(y), tri_list.index(z)
    return x_dex * 10 ** (3 * deg) + y_dex * 10 ** (2 * deg) + z_dex * 10 ** deg


def in_sphere(point, center, radius):
    '''returns a True if the point is inside a sphere with given center and radius'''
    return radius - distance(point, center) > 1 * 10 ** -10


def distance(point_1, point_2):
    '''Returnse the distance between 2 points in space'''
    x_1, y_1, z_1 = tuple(point_1)
    x_2, y_2, z_2 = tuple(point_2)

    return sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2 + (z_2 - z_1) ** 2)


def area(p1, p2, p3):
    '''Returns the area of the triangle using Heron's Formula'''
    a = distance(p1, p2)
    b = distance(p1, p3)
    c = distance(p2, p3)

    s = (a + b + c) / 2

    return sqrt(s * (s - a) * (s - b) * (s - c))


def format_output(triangle_list):
    '''formats the output so it is either a list of 3 points or a
    list of lists of 3 points
    '''
    list_out = []
    for item in triangle_list:
        list_out += [list(item)]
    if len(list_out) == 1:
        return list_out[0]
    else:
        return list_out


def biggest_triang_int(point_list, center, radius):
    valid_points = [point for point in point_list if in_sphere(point, center, radius)]

    if len(valid_points) < 3:
        return []

    triangles = [tri for tri in combinations(valid_points, r=3)]
    areas = [[area(tri[0], tri[1], tri[2]), tri] for tri in triangles]

    max_area = max(areas, key=lambda x: x[0])[0]
    num_tri = len(triangles)

    tri_w_max_area = [tri[1] for tri in areas if abs(tri[0] - max_area) < 10 ** -10]

    tri_vert = sorted(tri_w_max_area, key=lambda x: sort_key(point_list, x))

    tri_vert = format_output(tri_vert)

    return [num_tri, max_area, tri_vert]
