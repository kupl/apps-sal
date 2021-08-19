import sys
import numpy
from collections import OrderedDict
f = sys.stdin


def makeJump(op):
    p = op[1] - 1
    nj = 0
    for i in range(p + 1, n):
        dist = i - p
        if dist > 100:
            break
        else:
            vp = a[p]
            vi = a[i]
            for k in [x for x in list(jumps.keys()) if x <= p]:
                d = jumps[k]
                for k2 in d:
                    if p <= k2:
                        vp += d[k2]
            for k in [x for x in list(jumps.keys()) if x <= i]:
                d = jumps[k]
                for k2 in d:
                    if i <= k2:
                        vi += d[k2]
            if vp < vi:
                p = i
                nj += 1
        if nj >= op[2]:
            break
    print(p + 1)
    return


(n, q) = [int(x) for x in f.readline().split()]
a = [int(x) for x in f.readline().split()]
queries = []
jumps = {}
for _ in range(0, q):
    op = [int(x) for x in f.readline().split()]
    if op[0] == 1:
        makeJump(op)
    else:
        l = op[1] - 1
        r = op[2] - 1
        x = op[3]
        if not l in jumps:
            jumps[l] = {}
        if not r in jumps[l]:
            jumps[l][r] = 0
        jumps[l][r] += x
