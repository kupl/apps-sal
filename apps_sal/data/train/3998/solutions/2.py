import math


def area_of_polygon_inside_circle(circle_radius, number_of_sides):
    r = circle_radius
    s = number_of_sides
    a = s * r ** 2 * math.sin(2 * math.pi / s) / 2
    return round(a, 3)
