import sys
sys.setrecursionlimit(10 ** 6)
(n, m) = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    (u, v, c) = map(int, input().split())
    graph[u - 1].append((v - 1, c))
    graph[v - 1].append((u - 1, c))


def dfs(node):
    for (c_node, label) in graph[node]:
        if seen[c_node]:
            continue
        seen[c_node] = True
        if ans[node] == label:
            if label == 1:
                ans[c_node] = 2
            else:
                ans[c_node] = 1
        else:
            ans[c_node] = label
        dfs(c_node)


ans = [None] * n
ans[0] = 1
seen = [False] * n
seen[0] = True
dfs(0)
for i in ans:
    print(i)
