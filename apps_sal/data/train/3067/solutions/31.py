from functools import reduce
from operator import mul
def getVolumeOfCubiod(*n):
    return reduce(mul, n)

