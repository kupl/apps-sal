import sys
import bisect
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for i in range(n - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)

rooted = [[] for _ in range(n)]
que = [(0, -1)]
while que:
    node, parent = que.pop()
    for child in graph[node]:
        if child != parent:
            rooted[node].append(child)
            # rooted[child].append(node)
            que.append((child, node))
            # print(child + 1, node + 1)

table = [float('inf')] * n
lis = [None] * n


def dfs(node, length=0):
    p = bisect.bisect_left(table, a[node])
    table[p], old = a[node], table[p]
    length = max(p + 1, length)
    for child in rooted[node]:
        dfs(child, length)
    table[p] = old
    lis[node] = length


dfs(0)
print(*map(str, lis), sep="\n")
