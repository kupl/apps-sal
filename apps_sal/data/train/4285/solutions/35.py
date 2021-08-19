from math import hypot


def find_slope(points):
    return str((points[3] - points[1]) // (points[2] - points[0])) if points[2] != points[0] else 'undefined'
