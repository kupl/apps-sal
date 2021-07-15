#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    n = I()
    a = LI()
    a.sort()
    f = [1]*n
    p = 0
    ans = 0
    while p < n:
        while p < n and not f[p]:
            p += 1
        if p == n:
            break
        ans += 1
        for i in range(n):
            if a[i]%a[p] == 0:
                f[i] = 0
    print(ans)
    return

#B
def B():
    n = I()
    s = list(map(int, input()))
    g = LIR(n)
    ans = sum(s)
    for t in range(30000):
        for i in range(n):
            ai,bi = g[i]
            if t < bi:
                continue
            if (t-bi)%ai == 0:
                s[i] ^= 1
        su = sum(s)
        if ans < su:
            ans = su
    print(ans)
    return

#C
def C():
    t = I()
    for _ in range(t):
        n = I()
        s = list(map(int, input()))
        mi = [s[-1]]
        for i in s[:-1][::-1]:
            mi.append(min(mi[-1],i))
        mi = mi[::-1]
        ans = [None]*n
        for i in range(n):
            if mi[i] == s[i]:
                ans[i] = 1
            else:
                ans[i] = 2
        q = [s[i] for i in range(n) if ans[i] > 1]
        p = [q[i] for i in range(len(q))]
        p.sort()
        if p == q:
            print(*ans,sep = "")
        else:
            print("-")
    return

#D
def D():
    def root(x):
        if x == par[x]:
            return x
        par[x] = root(par[x])
        return par[x]

    def unite(x,y):
        x = root(x)
        y = root(y)
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

    n,k = LI()
    par = [i for i in range(n)]
    rank = [0]*n
    for i in range(k):
        x,y = LI()
        x -= 1
        y -= 1
        if root(x) != root(y):
            unite(x,y)
    size = [0]*n
    for i in range(n):
        size[root(i)] += 1
    ans = 0
    for i in size:
        if i > 0:
            ans += i-1
    print(k-ans)
    return

#E
def E():

    return

#F
def F():

    return

#G
def G():

    return

#H
def H():

    return

#Solve
def __starting_point():
    D()

__starting_point()
