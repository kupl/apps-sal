from math import hypot


def dropzone(fire, dropzones):
    return min(dropzones, key=lambda x: hypot(x[0] - fire[0], x[1] - fire[1]))
