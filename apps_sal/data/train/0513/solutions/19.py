
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    import math
    from math import gcd

    n = int(input())
    a = list(map(int, input().split()))
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        c, b = list(map(int, input().split()))
        adj[c - 1].append(b - 1)
        adj[b - 1].append(c - 1)

    res = [0] * n
    res[0] = 1

    def dfs(v, par, L):
        if v != 0:
            if a[v] > L[-1]:
                temp = -1
                L.append(a[v])
            else:
                temp = bisect_left(L, a[v])
                pre = L[temp]
                L[temp] = a[v]
        res[v] = len(L)
        for nv in adj[v]:
            if nv == par:
                continue
            dfs(nv, v, L)
        if v != 0:
            if temp == -1:
                L.pop(-1)
            else:
                L[temp] = pre

    L = [a[0]]
    dfs(0, -1, L)
    for i in range(n):
        print((res[i]))


def __starting_point():
    main()


__starting_point()
