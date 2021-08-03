# cook your dish here
from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

g = defaultdict(list)


def dfs(u, visited):
    visited[u] = True
    for v in g[u]:
        if not visited[v]:
            dfs(v, visited)


for _ in range(int(input())):
    (n, m) = map(int, input().split())
    g.clear()

    for _ in range(m):
        (u, v) = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    visited = [False] * n
    ans = 0
    for i in range(n):
        if not visited[i]:
            ans += 1
            dfs(i, visited)
    print(ans)
