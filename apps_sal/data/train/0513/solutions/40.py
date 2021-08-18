import bisect
import sys
sys.setrecursionlimit(10**7)

INF = 10**18

n = int(input())
a = list(int(x) for x in input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)


def dfs(now, par):
    idx = bisect.bisect_left(dp, a[now])
    tmp = dp[idx]
    dp[idx] = a[now]
    if ans[par] <= idx:
        ans[now] = idx
    else:
        ans[now] = ans[par]

    for i in g[now]:
        if i != par:
            dfs(i, now)
    dp[idx] = tmp


ans = [0] * n
dp = [-INF] + [INF] * n
dfs(0, -1)
for a in ans:
    print(a)
