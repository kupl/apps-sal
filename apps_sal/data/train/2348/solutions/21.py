#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
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

def solve():
    n = I()
    x = LI()
    L = I()
    q = I()
    p = [[] for i in range(n)]
    for i in range(n):
        xi = x[i]
        l = i
        r = n
        while r-l > 1:
            m = (l+r) >> 1
            xm = x[m]
            if xm-xi <= L:
                l = m
            else:
                r = m
        p[i].append(l)
    N = 20
    for j in range(N):
        for i in range(n):
            p[i].append(p[p[i][-1]][-1])
    for i in range(q):
        a,b = LI()
        a -= 1
        b -= 1
        a,b = min(a,b),max(a,b)
        ans = 1
        for j in range(N)[::-1]:
            if p[a][j] < b:
                a = p[a][j]
                ans += 1<<j
        print(ans)
    return

#Solve
def __starting_point():
    solve()

__starting_point()
