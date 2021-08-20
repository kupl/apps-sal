import collections
from sys import *
import bisect as bs
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = 1
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = []
        d[a[i]].append(i)
    l = list(d.keys())
    l.sort()
    c = 0
    for j in l:
        ln = len(d[j])
        v = bs.bisect_left(d[j], c)
        if v == ln:
            c = d[j][0] + 1
            s += 1
            continue
        c = d[j][v] + 1
    print(s)
