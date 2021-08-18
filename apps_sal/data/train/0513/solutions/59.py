from collections import deque
from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)
n = int(input())
a = list(map(int, input().split()))
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)
stack = deque([])
inf = 10**18
lis = [inf] * (n + 1)
ans = [0 for _ in range(n)]
visited = [True] * n


def dfs(s):
    visited[s] = False
    idx = bisect_left(lis, a[s])
    stack.append((idx, lis[idx]))
    lis[idx] = a[s]
    ans[s] = bisect_left(lis, inf)
    for x in edge[s]:
        if visited[x]:
            dfs(x)
    idx, val = stack.pop()
    lis[idx] = val


dfs(0)
for i in range(n):
    print(ans[i])
