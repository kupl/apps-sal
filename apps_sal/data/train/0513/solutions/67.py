from bisect import bisect_right, bisect_left
import sys
sys.setrecursionlimit(10101000)
n = int(input())
*a, = list(map(int, input().split()))
t = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    t[u].append(v)
    t[v].append(u)

INF = 10**10
eps = 0.1
his = [(-1, -1)] * (n + 1)
lis = [INF] * (n + 1)
ans = [-1] * n


def dfs(v):
    l = bisect_left(lis, a[v])
    his[v] = (l, lis[l])
    lis[l] = a[v]
    ans[v] = bisect_left(lis, INF)
    for u in t[v]:
        if ans[u] < 0:
            dfs(u)
    ll, pre = his[v]
    lis[ll] = pre


dfs(0)
for ai in ans:
    print(ai)
