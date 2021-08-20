from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


def I():
    return int(sys.stdin.readline())


def LS():
    return [list(x) for x in sys.stdin.readline().split()]


def S():
    res = list(sys.stdin.readline())
    if res[-1] == '\n':
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

    def check(x, y):
        return (x == 0) | (x == w) | (y == 0) | (y == h)
    (w, h, n) = LI()
    px0 = []
    pxw = []
    py0 = []
    pyh = []
    for i in range(1, n + 1):
        (x, y, s, t) = LI()
        if check(x, y) & check(s, t):
            if x == 0:
                px0.append((y, i))
            elif x == w:
                pxw.append((-y, i))
            elif y == 0:
                py0.append((-x, i))
            else:
                pyh.append((x, i))
            if s == 0:
                px0.append((t, i))
            elif s == w:
                pxw.append((-t, i))
            elif t == 0:
                py0.append((-s, i))
            else:
                pyh.append((s, i))
    px0.sort()
    pxw.sort()
    py0.sort()
    pyh.sort()
    p = px0 + pyh + pxw + py0
    q = deque()
    for (x, i) in p:
        if q:
            qi = q.pop()
            if qi != i:
                q.append(qi)
                q.append(i)
        else:
            q.append(i)
    if q:
        print('NO')
    else:
        print('YES')
    return


def __starting_point():
    solve()


__starting_point()
