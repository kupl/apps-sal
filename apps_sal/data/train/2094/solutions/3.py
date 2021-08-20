from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect


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
    n = I()
    s = S()
    d = defaultdict(lambda: 0)
    for i in s:
        d[i] += 1
    ans = [1] * d['n']
    d['o'] -= d['n']
    ans += [0] * d['o']
    print(*ans)
    return


def B():
    return


def C():
    return


def D():
    return


def E():
    return


def F():
    return


def G():
    return


def __starting_point():
    A()


__starting_point()
