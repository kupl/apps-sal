from math import sin, pi


def area_of_polygon_inside_circle(r, n):
    return round(n * r ** 2 * sin(2 * pi / n) / 2, 3)
