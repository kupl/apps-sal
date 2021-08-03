from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)
INF = 10**18


def dfs(v, p, max_):
    b = bisect_left(dp, a[v])
    memo = (b, dp[b])
    dp[b] = a[v]
    if b > max_:
        max_ = b
    ans[v] = max_
    for nv in G[v]:
        if nv == p:
            continue
        dfs(nv, v, max_)
    dp[memo[0]] = memo[1]


N = int(input())
a = list(map(int, input().split()))
G = [[] for i in range(N)]
for i in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u].append(v)
    G[v].append(u)
dp = [INF] * (N + 1)
dp[0] = -1
ans = [-1] * N
dfs(0, -1, 0)
print(*ans, sep='\n')
