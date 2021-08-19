from math import radians, sin, cos


def coordinates(degrees, radius):
    angle = radians(degrees)
    return tuple((round(f(angle) * radius, 10) for f in (cos, sin)))
