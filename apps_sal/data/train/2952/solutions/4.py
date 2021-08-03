from math import sqrt


def dropzone(p, dropzones):
    distances = {sqrt((p[0] - dz[0])**2 + (p[1] - dz[1])**2): dz for dz in dropzones}
    return distances[min(list(distances.keys()))]
