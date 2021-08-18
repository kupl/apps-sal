import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()


def resolve():
    N, M = LI()
    p = LI_()
    G = [[] for _ in range(N)]
    for _ in range(M):
        x, y = LI_()
        G[x].append(y)
        G[y].append(x)

    visited = [False] * N

    def dfs(c, tmp):
        visited[c] = True
        tmp.append(c)
        for n in G[c]:
            if not visited[n]:
                dfs(n, tmp)

    c = []
    for i in range(N):
        if not visited[i]:
            tmp = []
            dfs(i, tmp)
            c.append(tmp)

    ans = sum([len({p[j] for j in i} & set(i)) for i in c])
    print(ans)


def __starting_point():
    resolve()


__starting_point()
