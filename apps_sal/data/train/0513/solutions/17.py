
import numpy as np
import sys
sys.setrecursionlimit(10 ** 6)


INF = 10 ** 10

N = int(input())
A = list(map(int, input().split()))
uv = [list(map(int, input().split())) for _ in range(N - 1)]

link = [[] for _ in range(N + 1)]
for u, v in uv:
    link[u].append(v)
    link[v].append(u)


def dfs(l, dp, pre, v):
    idx = np.searchsorted(dp, A[v - 1])
    l[v] = max(idx, l[pre])
    bef = dp[idx]
    dp[idx] = A[v - 1]

    for x in link[v]:
        if x != pre:
            dfs(l, dp, v, x)

    dp[idx] = bef


def main():
    l = [0] * (N + 1)
    dp = np.full(N + 1, INF)
    dp[0] = 0
    dfs(l, dp, 0, 1)
    for ans in l[1:]:
        print(ans)


def __starting_point():
    main()


__starting_point()
