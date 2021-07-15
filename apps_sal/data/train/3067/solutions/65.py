from functools import reduce
from operator import mul

def getVolumeOfCubiod(*a):
    return reduce(mul, a, 1)

