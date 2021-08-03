from functools import reduce


def getVolumeOfCubiod(*a):
    return reduce(lambda accum, next_item: accum * next_item, a)
