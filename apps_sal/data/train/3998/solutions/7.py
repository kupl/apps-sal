from math import pi, sin


def area_of_polygon_inside_circle(r, n):
    return round(0.5 * n * r ** 2 * sin(2 * pi / n), 3)
