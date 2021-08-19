from math import sin, cos, radians


def coordinates(deg, r):
    theta = radians(deg)
    return tuple((round(r * f(theta), 10) for f in (cos, sin)))
