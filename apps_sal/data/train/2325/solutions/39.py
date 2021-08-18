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

INF = 10 ** 20
MOD = 10 ** 9 + 7


def ni(): return int(sys.stdin.readline())
def ns(): return list(map(int, sys.stdin.readline().split()))
def na(): return list(map(int, sys.stdin.readline().split()))
def na1(): return list([int(x) - 1 for x in sys.stdin.readline().split()])


def main():
    s = input()
    t = input()

    scnt = [[0, 0] for _ in range(len(s) + 1)]
    for i, si in enumerate(s):
        if si == "A":
            scnt[i + 1] = [scnt[i][0] + 1, scnt[i][1]]
        else:
            scnt[i + 1] = [scnt[i][0], scnt[i][1] + 1]

    tcnt = [[0, 0] for _ in range(len(t) + 1)]
    for i, ti in enumerate(t):
        if ti == "A":
            tcnt[i + 1] = [tcnt[i][0] + 1, tcnt[i][1]]
        else:
            tcnt[i + 1] = [tcnt[i][0], tcnt[i][1] + 1]

    q = ni()
    for _ in range(q):
        a, b, c, d = ns()
        a, b, c, d = a - 1, b, c - 1, d

        sa = scnt[b][0] - scnt[a][0]
        sb = scnt[b][1] - scnt[a][1]

        sa %= 3
        sb %= 3
        mn = min(sa, sb)
        sa -= mn
        sb -= mn
        if sa == 2:
            sb = 1
            sa = 0
        elif sb == 2:
            sa = 1
            sb = 0

        ta = tcnt[d][0] - tcnt[c][0]
        tb = tcnt[d][1] - tcnt[c][1]
        ta %= 3
        tb %= 3
        mn = min(ta, tb)
        ta -= mn
        tb -= mn
        if ta == 2:
            tb = 1
            ta = 0
        elif tb == 2:
            ta = 1
            tb = 0

        if sa == ta and sb == tb:
            print("YES")
        else:
            print("NO")


def __starting_point():
    main()


__starting_point()
