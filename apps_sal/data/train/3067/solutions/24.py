from functools import reduce


def getVolumeOfCubiod(l, w, h):
    return reduce(lambda x, y: x * y, [l, w, h])
