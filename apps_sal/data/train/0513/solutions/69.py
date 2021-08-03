from bisect import bisect_left
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def main(N, a, tr):
    ans = [0] * N
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    maxa = max(a) + 1

    def dfs(p, v, dp):
        i = bisect_left(dp, a[v])
        tmp = dp[i]
        dp[i] = a[v]
        ans[v] = bisect_left(dp, maxa) - 1
        for nv in tr[v]:
            if nv != p:
                dfs(v, nv, dp)
        dp[i] = tmp
    dfs(-1, 0, dp)
    print(*ans, sep='\n')


def __starting_point():
    N = int(input())
    a = list(map(int, input().split()))
    tr = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u, v = u - 1, v - 1
        tr[u].append(v)
        tr[v].append(u)
    main(N, a, tr)


__starting_point()
