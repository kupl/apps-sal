from functools import reduce

getVolumeOfCubiod = lambda l,w,h: reduce(lambda x,y:x*y, [l,w,h])
