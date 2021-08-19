import math


def coordinates(degrees, radius):
    theta = math.radians(degrees)
    x = math.cos(theta) * radius
    y = math.sin(theta) * radius
    return (round(x, 10), round(y, 10))
