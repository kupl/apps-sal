# LIS on Tree

from collections import deque
import bisect
import sys
sys.setrecursionlimit(10**7)

N = int(input())
V = list(map(int, input().split()))
V.insert(0, 0)
visited = [False for i in range(N + 1)]
inf = 10**18
dp = [inf for i in range(N + 1)]
ans = [-1 for i in range(N + 1)]
stack = deque()

G = [[] for i in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)


def dfs(s_node):
    visited[s_node] = True
    # dp値の更新
    value = V[s_node]
    index = bisect.bisect_left(dp, value)
    old_value = dp[index]
    dp[index] = value
    ans[s_node] = bisect.bisect_right(dp, inf - 1)
    stack.append((index, old_value, value))
    for child in G[s_node]:
        if visited[child] == False:
            dfs(child)
    # 帰りがけにバックトラックを行う
    index, old_value, value = stack.pop()
    dp[index] = old_value


dfs(1)

for i in range(1, N + 1):
    print(ans[i])
