from math import sqrt


def ellipse_contains_point(f0, f1, l, p):
    return distance(f0, p) + distance(f1, p) <= l


def distance(p0, p1):
    return sqrt(pow(p0['x'] - p1['x'], 2) + pow(p0['y'] - p1['y'], 2))
