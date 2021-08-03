from operator import mul
from functools import reduce, partial


def getVolumeOfCubiod(*args):
    return partial(reduce, mul)(args)
