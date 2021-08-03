from collections import defaultdict


def dfs(graph, i):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            dfs(graph, j)


n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split()))[1:])
graph = defaultdict(list)
for i in range(n):
    for j in range(i + 1, n):
        c = len(set(arr[i]).intersection(set(arr[j])))
        if c >= k:
            graph[i].append(j)
            graph[j].append(i)
visited = [False] * n
dfs(graph, 0)
print(visited.count(True))
