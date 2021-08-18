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


def dist(l1, l2):
    return max(0, math.sqrt((l1[0] - l2[0])**2 + (l1[1] - l2[1])**2) - l1[2] - l2[2])


def main():
    xs, ys, xt, yt = ns()
    n = ni()
    pos = [na() for _ in range(n)]
    pos.insert(0, [xs, ys, 0])
    pos.append([xt, yt, 0])
    d = [[dist(pos[i], pos[j]) for i in range(n + 2)] for j in range(n + 2)]

    mind = [INF for _ in range(n + 2)]
    visited = [False for _ in range(n + 2)]

    hq = []
    heapq.heappush(hq, (0, 0))
    mind[0] = 0
    while hq:
        dis, idx = heapq.heappop(hq)
        if visited[idx]:
            continue
        visited[idx] = True

        if idx == n + 1:
            break
        for i in range(n + 2):
            if i == idx:
                continue
            ndist = dis + d[idx][i]
            if ndist < mind[i] and ndist < mind[n + 1]:
                mind[i] = ndist
                heapq.heappush(hq, (ndist, i))

    print((mind[n + 1]))


def __starting_point():
    main()


__starting_point()
