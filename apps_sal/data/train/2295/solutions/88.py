import typing
import sys
import math
import collections
import bisect
import itertools
import heapq
import decimal
import copy
import operator

# sys.setrecursionlimit(10000001)
INF = 10 ** 20
MOD = 10 ** 9 + 7
# MOD = 998244353
# buffer.readline()


def ni(): return int(sys.stdin.readline())
def ns(): return list(map(int, sys.stdin.readline().split()))
def na(): return list(map(int, sys.stdin.readline().split()))
def na1(): return list([int(x) - 1 for x in sys.stdin.readline().split()])


# ===CODE===

def main():
    n = ni()
    d = []
    x = []
    y = []
    s = []
    for _ in range(n):
        a, b = ns()
        c = a - b
        d.append([a, b, c])
        x.append(a)
        y.append(b)
        if c > 0:
            s.append(b)
    d.sort(key=lambda x: x[2])

    if x == y:
        print((0))
        return

    ans = sum(x) - min(s)
    print(ans)


def __starting_point():
    main()


__starting_point()
