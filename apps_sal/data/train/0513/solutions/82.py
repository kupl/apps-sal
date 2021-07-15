from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)

N = int(input())
a = list(map(int, input().split()))

G = [[] for i in range(N)]
for i in range(N-1):
    uv = list(map(lambda x: int(x)-1, input().split()))
    G[uv[0]].append(uv[1])
    G[uv[1]].append(uv[0])

dp = [10 ** 10 for _ in range(N+1)]
dp[0] = -1
ans = [-1] * N

def dfs(v, p, max_):
    i = bisect_left(dp, a[v])
    memo = (i, dp[i])
    dp[i] = a[v]

    if i > max_:
        max_ = i
    ans[v] = max_

    for nv in G[v]:
        if nv == p:
            continue
        dfs(nv, v, max_)
    dp[memo[0]] = memo[1]

dfs(0, -1, 0)

print(*ans, sep='\n')

