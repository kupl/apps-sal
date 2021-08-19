from sys import setrecursionlimit
from bisect import bisect_left
setrecursionlimit(10 ** 6)
INF = float('inf')
(N, *I) = map(int, open(0).read().split())
(A, UV) = (I[:N], I[N:])
E = [[] for _ in range(N + 1)]
for (u, v) in zip(*[iter(UV)] * 2):
    E[u - 1].append(v - 1)
    E[v - 1].append(u - 1)
dp = [INF] * N
ans = [0] * N


def dfs(cur, visited):
    idx = bisect_left(dp, A[cur])
    pre = dp[idx]
    dp[idx] = A[cur]
    ans[cur] = bisect_left(dp, INF)
    for c in E[cur]:
        if c != visited:
            dfs(c, cur)
    dp[idx] = pre


dfs(0, -1)
for a in ans:
    print(a)
