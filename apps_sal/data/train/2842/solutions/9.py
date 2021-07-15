from math import sqrt

def coordinates(p1, p2, precision=0):
    x1, y1 = p1
    x2, y2 = p2
    distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return round(distance, precision)
