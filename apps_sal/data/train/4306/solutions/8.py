import math


def coordinates(degrees, radius):
    if degrees != 0:
        degrees = math.pi / (180 / degrees)
    else:
        degrees = 0
    return (round(radius * math.cos(degrees), 10), round(radius * math.sin(degrees), 10))
