from sys import stdin as I
from collections import defaultdict


def ints():
    return [int(s) for s in I.readline().split()]


T = ints()[0]
while T:
    T -= 1
    n = ints()
    c = defaultdict(int)
    for x in ints():
        c[x] += 1
    rv = (0, 0)
    for (val, ct) in list(c.items()):
        if ct > rv[1]:
            rv = (val, ct)
        elif ct == rv[1] and val < rv[0]:
            rv = (val, ct)
    print(rv[0], rv[1])
