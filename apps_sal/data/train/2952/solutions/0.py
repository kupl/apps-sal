from math import hypot


def dropzone(fire, dropzones):
    return min(dropzones, key=lambda p: hypot(p[0] - fire[0], p[1] - fire[1]))
