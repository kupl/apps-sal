from functools import reduce
from operator import mul

getVolumeOfCubiod = lambda *ns: reduce(mul, ns)
