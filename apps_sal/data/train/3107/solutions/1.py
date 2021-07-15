def distance(p1, p2):
    from functools import reduce
    from math import hypot
    if not p1 or len(p1) != len(p2): return -1
    return reduce(hypot, (x-y for x,y in zip(p1, p2)))
