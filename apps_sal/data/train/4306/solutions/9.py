from math import radians, sin, cos


def coordinates(degrees, radius):
    return (round(radius * cos(radians(degrees)), 10), round(radius * sin(radians(degrees)), 10))
