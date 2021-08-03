#!/usr/bin/env python3
import sys

sys.setrecursionlimit(101010)


def dfs(v, adj_list, depth, visited):
    visited[v] = True
    x = depth
    for w in adj_list[v]:
        if not visited[w]:
            x += dfs(w, adj_list, depth + 1, visited)

    return x


def solve(n, d):

    if n < 7:
        print((-1))
        return

    d.sort()
    w = [1] * n
    edges = []
    adj_list = [[] for _ in range(n)]
    for j in range(n - 1, 0, -1):
        di, i = d[j]
        pdi = di - n + 2 * w[i]
        p = None
        lo, hi = 0, j
        while lo < hi:
            mid = (lo + hi) // 2
            xdi, xi = d[mid]
            if xdi == pdi:
                p = xi
                break
            elif xdi < pdi:
                lo = mid + 1
            else:
                hi = mid
        if p is None:
            print((-1))
            return
        u, v = i, p
        if v < u:
            u, v = v, u
        edges.append((u + 1, v + 1))
        adj_list[u].append(v)
        adj_list[v].append(u)
        w[p] += w[i]

    d0, r = d[0]
    visited = [False] * n
    x = dfs(r, adj_list, 0, visited)
    if x != d0:
        print((-1))
        return

    edges.sort()
    for uv in edges:
        u, v = uv
        print(('{} {}'.format(u, v)))


def main():
    n = input()
    n = int(n)
    d = []
    for i in range(n):
        di = input()
        di = int(di)
        d.append((di, i))

    solve(n, d)


def __starting_point():
    main()


__starting_point()
