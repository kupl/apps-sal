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


def A():
    return


def B():
    return


def C():
    (n, c) = LI()
    a = LI()
    b = LI()
    s = [[0] * (c + 1) for i in range(n)]
    for i in range(n):
        (ai, bi) = (a[i], b[i])
        for x in range(ai, bi + 1):
            e = 1
            for k in range(c + 1):
                s[i][k] += e
                if s[i][k] >= mod:
                    s[i][k] %= mod
                e *= x
                if e >= mod:
                    e %= mod
    dp = [[0] * (c + 1) for i in range(n)]
    for k in range(c + 1):
        dp[0][k] = s[0][k]
    for i in range(1, n):
        for k in range(c + 1):
            for j in range(k + 1):
                dp[i][k] += dp[i - 1][j] * s[i][k - j]
                if dp[i][k] >= mod:
                    dp[i][k] %= mod
    print(dp[-1][c])
    return


def D():
    return


def E():
    return


def F():
    return


def __starting_point():
    C()


__starting_point()
