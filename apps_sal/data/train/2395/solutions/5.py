from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return [list(x) for x in sys.stdin.readline().split()]


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
    t = I()
    for _ in range(t):
        n = I()
        x = list(map(int, input()))
        a = []
        b = []
        f = 0
        for i in x:
            if not i:
                a.append(0)
                b.append(0)
            elif i == 2:
                if f:
                    a.append(0)
                    b.append(2)
                else:
                    a.append(1)
                    b.append(1)
            else:
                if f:
                    a.append(0)
                    b.append(1)
                else:
                    a.append(1)
                    b.append(0)
                    f = 1
        print(*a, sep="")
        print(*b, sep="")
    return


def __starting_point():
    solve()


__starting_point()
