from functools import reduce
getVolumeOfCubiod = lambda *dimensions: reduce(lambda x, y: x * y, dimensions)
