from math import sin, pi


def area_of_polygon_inside_circle(radius, sides):
    return round(sides * radius * radius * sin(pi * (sides - 2) / sides) / 2, 3)
