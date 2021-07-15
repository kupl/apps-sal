from math import cos, sin, radians

def coordinates(deg, r, precision=10):
    x, y = r * cos(radians(deg)), r * sin(radians(deg))
    return round(x, precision), round(y, precision)
