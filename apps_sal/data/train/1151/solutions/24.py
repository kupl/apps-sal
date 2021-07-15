def dfs(u):
    visited[u] = 1
    for i in graph[u]:
        if visited[i] == 0:
            dfs(i)

for _ in range(int(input())):
    N, M = map(int, input().split())
    graph = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    ccnum = 0
    visited = [0] * N
    for pp in range(N):
        if visited[pp] == 0:
            dfs(pp)
            ccnum += 1
    print(ccnum)
