# F - LIS on Tree
import bisect
import sys
sys.setrecursionlimit(10**7)

INF = 10**18

n = int(input())
a = list(int(x) for x in input().split())
g = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

def dfs(now, par):
    idx = bisect.bisect_left(dp, a[now])    
    tmp = dp[idx]
    dp[idx] = a[now]
    # 親のLIS以上であれば、その値で更新
    if ans[par] <= idx:
        ans[now] = idx
    # そうでなければ親のLISを引き継ぐ
    else:
        ans[now] = ans[par]

    for i in g[now]:
        if i!=par:
            # 次にみる頂点と、自分（親）の情報を渡す
            dfs(i, now)
    dp[idx] = tmp

ans = [0] * n
dp = [-INF] + [INF] * n
dfs(0, -1)
for a in ans:
    print(a)

