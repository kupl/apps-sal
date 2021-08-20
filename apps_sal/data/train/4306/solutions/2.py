from math import cos, radians, sin


def coordinates(th, r):
    return tuple((round(r * f(radians(th)), 10) for f in (cos, sin)))
