from math import pi, sin


def area_of_polygon_inside_circle(r, n):
    return round(n * r * r * sin(pi * 2 / n) / 2, 3)
