import math


def sum_circles(*args):
    totalArea = 0
    for arg in args:
        area = ((arg / 2.0)**2.0) * math.pi
        totalArea += area
    return "We have this much circle: " + str(int(round(totalArea)))
