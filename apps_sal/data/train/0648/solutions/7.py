import sys
import numpy as np
from collections import OrderedDict
f = sys.stdin
(n, q) = [int(x) for x in f.readline().split()]
a = [int(x) for x in f.readline().split()]
L = [0] * (n + 1)
R = [0] * (n + 1)
for _ in range(0, q):
    op = [int(x) for x in f.readline().split()]
    if op[0] == 1:
        p = op[1] - 1
        nj = 0
        vis = L[p] - R[p]
        vp = a[p] + vis
        for i in range(p + 1, n):
            dist = i - p
            if dist > 100:
                break
            else:
                vis += L[i] - R[i]
                vi = a[i] + vis
                if vp < vi:
                    p = i
                    vp = vi
                    nj += 1
                    if nj >= op[2]:
                        break
        print(p + 1)
    else:
        l = op[1] - 1
        r = op[2] - 1
        L[l] += op[3]
        R[r + 1] += op[3]
