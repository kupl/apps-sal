import sys

import math
import collections
from sys import stdin, stdout, setrecursionlimit
import bisect as bs
setrecursionlimit(2**20)
M = 10**9 + 7

T = int(stdin.readline())


def func(n, a):
    q = n // a
    r = n % a
    if(r != 0):
        return((10 * r) // a)
    else:
        return(int(str(q)[0]))


for _ in range(T):
    n = int(stdin.readline())
    a, b, c = list(map(int, stdin.readline().split()))
    g = []
    for i in range(11):
        g.append([0, 0, 0])
        g[i][0] = func(i, a)
        g[i][1] = func(i, b)
        g[i][2] = func(i, c)
    l = [n]
    l.append(func(l[-1], a))
    l.append(func(l[-1], b))
    l.append(func(l[-1], c))
    cur = l[-1]
    ind = 0
    d = {}
    st = 4
    while((cur, ind) not in d):
        d[(cur, ind)] = st
        cur = g[cur][ind]
        ind = (ind + 1) % 3
        l.append(cur)
        st += 1
    st = d[(cur, ind)]
    en = len(l)
    sec = en - st
    q = int(stdin.readline())
    for i in range(q):
        qi = int(stdin.readline())
        if(qi <= st):
            print(l[qi])
            continue
        ans = st + (qi - st) % sec
        print(l[ans])
