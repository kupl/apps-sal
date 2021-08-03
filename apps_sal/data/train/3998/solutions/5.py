from math import sin, tau


def area_of_polygon_inside_circle(circle_radius, number_of_sides):
    s = number_of_sides / 2 * circle_radius ** 2 * sin((tau / number_of_sides))
    return round(s, 3)
