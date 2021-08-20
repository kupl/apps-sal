from bisect import bisect_left
import sys
sys.setrecursionlimit(10 ** 9)
N = int(input())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(N - 1):
    (u, v) = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
root = 0
ans = [0] * N
check = [False] * N
check[root] = True
memo = [None] * N
INF = 10 ** 10
dp = [INF] * N


def dfs(x):
    tmp = bisect_left(dp, A[x])
    memo[x] = (tmp, dp[tmp])
    dp[tmp] = A[x]
    ans[x] = bisect_left(dp, INF)
    for next_ in G[x]:
        if check[next_]:
            continue
        check[next_] = True
        dfs(next_)
    (j, a) = memo[x]
    dp[j] = a


dfs(root)
print(*ans, sep='\n')
