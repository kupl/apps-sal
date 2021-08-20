def dfs(graph, i):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            dfs(graph, j)


(N, K) = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
nodes = [[] for _ in range(N)]
for i in range(N - 1):
    for j in range(i + 1, N):
        count = len(set(arr[i]).intersection(set(arr[j])))
        if count >= K:
            nodes[i].append(j)
            nodes[j].append(i)
visited = [False] * N
dfs(nodes, 0)
print(visited.count(True))
