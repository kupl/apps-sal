from math import floor, degrees, acos, pi, sin, radians


def calc_theta(a, b):
    return degrees(acos(a / b))


def calc_circle_segment_area(r, alpha):
    return pi * r**2 * (alpha / 360)


def calc_triangle_area(r, alpha):
    return (r**2 * sin(alpha)) / 2


def calc_cylinder_height(r, vt):
    return vt / (pi * r**2)


def tankvol(h, d, vt):
    r = d / 2

    theta = calc_theta(r - h, r)
    angle = theta * 2

    segment_area = calc_circle_segment_area(r, angle)
    triangle_area = calc_triangle_area(r, radians(angle))
    cylinder_height = calc_cylinder_height(r, vt)

    liquid_area = segment_area - triangle_area
    liquid_volume = liquid_area * cylinder_height

    return floor(liquid_volume)
