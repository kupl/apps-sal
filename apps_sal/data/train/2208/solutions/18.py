from queue import Queue
'\ndef dfs(graphs, visited, here):\n    if visited[here] == False:\n        visited[here] = True\n        for next in graphs[here]:\n            if visited[next] == False:\n                dfs(graphs, visited, next)\n\ndef dfsAll(graphs, visited, N):\n    ret = 0\n    for here in range(1, N+1):\n        if visited[here] == False:\n            ret += 1\n            dfs(graphs, visited, here)\n    return ret\n'
'\ndef bfs(graphs, visited, here):\n    if visited[here] == False:\n        q = Queue()\n        q.put(here)\n        while q.qsize() > 0:\n            here = q.get()\n            for next in graphs[here]:\n                if visited[next] == False:\n                    visited[next] = True\n                    q.put(next)\n\ndef bfsAll(graphs, visited, N):\n    ret = 0\n    for here in range(1, N+1):\n        if visited[here] == False:\n            ret += 1\n            bfs(graphs, visited, here)\n    return ret\n'
(N, K) = list(map(int, input().strip().split(' ')))
snacks = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]
for k in range(K):
    (a, b) = list(map(int, input().strip().split(' ')))
    snacks[a].append(b)
    snacks[b].append(a)
q = Queue()
components = 0
for here in range(1, N + 1):
    if visited[here] == False:
        visited[here] = True
        for there in snacks[here]:
            if visited[there] == False:
                visited[there] = True
                q.put(there)
        while q.qsize() > 0:
            here = q.get()
            for there in snacks[here]:
                if visited[there] == False:
                    visited[there] = True
                    q.put(there)
        components += 1
ret = K - (N - components)
print(ret)
