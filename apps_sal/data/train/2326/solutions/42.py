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

# buffer.readline()はこどふぉで死ぬ


def ni(): return int(sys.stdin.readline())
def ns(): return list(map(int, sys.stdin.readline().split()))
def na(): return list(map(int, sys.stdin.readline().split()))
def na1(): return list([int(x)-1 for x in sys.stdin.readline().split()])


# ===CODE===

def main():
    n = ni()
    ta = na()
    a = []
    for i, ai in enumerate(ta):
        a.append([ai, -i])
    a.sort(reverse=True)
    a.append([0, 0])
    cnt = [0 for _ in range(n)]

    idx = 0
    remain = a[0][0]
    minval = -a[0][1]
    while idx < n:
        while a[idx][0] == remain:
            idx += 1
        cnt[minval] += (remain-a[idx][0])*idx

        remain = a[idx][0]
        minval = min(minval, -a[idx][1])

    for c in cnt:
        print(c)


def __starting_point():
    main()

__starting_point()
