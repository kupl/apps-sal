import sys
import numpy
f = sys.stdin

n, q = [int(x) for x in f.readline().split()]
a = [int(x) for x in f.readline().split()]
t2 = []
for _ in range(0, q):
    op = [int(x) for x in f.readline().split()]
    if op[0] == 1:
        p = op[1] - 1
        jumps = 0
        for i in range(p + 1, n):
            dist = i - p
            if dist > 100:
                break
            else:
                vp = a[p]
                vi = a[i]
                for arr2 in t2:
                    l = arr2[1] - 1
                    r = arr2[2] - 1
                    if p >= l and p <= r:
                        vp += arr2[3]
                    if i >= l and i <= r:
                        vi += arr2[3]
                if vp < vi:
                    p = i
                    jumps += 1
            if jumps >= op[2]:
                break
        print(p + 1)
    else:
        t2.append(op)
