from collections import namedtuple


def distance_between_points(a, b):
    return ((b.x - a.x) ** 2 + (b.y - a.y) ** 2 + (b.z - a.z) ** 2) ** 0.5
