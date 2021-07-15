from math import gcd
from functools import reduce
from itertools import cycle

def robot_walk(a):
    g = reduce(gcd, a)
    a = [x//g for x in a]
    it = cycle([1j, 1, -1j, -1])
    seen = {0}
    pos = 0
    for x in a:
        d = next(it)
        for i in range(x):
            pos += d
            if pos in seen:
                return True
            seen.add(pos)
    return False
