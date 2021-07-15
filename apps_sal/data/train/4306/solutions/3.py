from math import cos, sin, radians

def coordinates(d, r):
    return round(r * cos(radians(d)), 10), round(r * sin(radians(d)), 10)
