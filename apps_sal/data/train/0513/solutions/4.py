from bisect import bisect_left
import sys
sys.setrecursionlimit(10 ** 9)
n = int(input())
a = list(map(int, input().split()))
result = [-1 for _ in range(n)]
tree = [[] for _ in range(n)]
for _i in range(n - 1):
    (u, v) = map(int, input().split())
    (u, v) = (u - 1, v - 1)
    tree[u].append(v)
    tree[v].append(u)
INF = float('inf')
dp = [INF for _i in range(n + 1)]


def dfs(p, x):
    i = bisect_left(dp, a[p])
    old = dp[i]
    dp[i] = a[p]
    result[p] = bisect_left(dp, INF)
    for j in tree[p]:
        if j != x:
            dfs(j, p)
    dp[i] = old


dfs(0, -1)
for i in result:
    print(i)
