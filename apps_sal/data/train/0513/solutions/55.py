#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
from bisect import bisect_left
INF = float("inf")


from collections import defaultdict


class Graph(object):
    def __init__(self, N):
        self.N = N
        self.E = defaultdict(list)

    def add_edge(self, f, t, w=1):
        self.E[f].append((t, w))
        self.E[t].append((f, w))


def solve(N: int, a: "List[int]", u: "List[int]", v: "List[int]"):

    g = Graph(N)
    for x, y in zip(u, v):
        g.add_edge(x-1, y-1)

    ans = [0]*N

    dp = [INF]*N
    event = []
    var = {"last": 0}

    def dfs(curr, par):
        i = bisect_left(dp, a[curr])
        if dp[i] > a[curr]:
            if dp[i] == INF:
                var["last"] = i
            event.append((curr, i, dp[i]))
            dp[i] = a[curr]

        ans[curr] = var["last"]+1

        for child, w in g.E[curr]:
            if child == par:
                continue
            dfs(child, curr)

        c, i, v = event[-1]
        if c == curr:
            dp[i] = v
            if v == INF:
                var["last"] = i-1
            event.pop()

    dfs(0, -1)
    print(*ans, sep="\n")

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    u = [int()] * (N - 1)  # type: "List[int]"
    v = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, a, u, v)


def __starting_point():
    main()

__starting_point()
