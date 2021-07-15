from queue import Queue
"""
def dfs(graphs, visited, here):
    if visited[here] == False:
        visited[here] = True
        for next in graphs[here]:
            if visited[next] == False:
                dfs(graphs, visited, next)

def dfsAll(graphs, visited, N):
    ret = 0
    for here in range(1, N+1):
        if visited[here] == False:
            ret += 1
            dfs(graphs, visited, here)
    return ret
"""
"""
def bfs(graphs, visited, here):
    if visited[here] == False:
        q = Queue()
        q.put(here)
        while q.qsize() > 0:
            here = q.get()
            for next in graphs[here]:
                if visited[next] == False:
                    visited[next] = True
                    q.put(next)

def bfsAll(graphs, visited, N):
    ret = 0
    for here in range(1, N+1):
        if visited[here] == False:
            ret += 1
            bfs(graphs, visited, here)
    return ret
"""
N, K = list(map(int,input().strip().split(' ')))
snacks = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]
for k in range(K):
    a, b = list(map(int,input().strip().split(' ')))
    snacks[a].append(b)
    snacks[b].append(a)
q = Queue()
components = 0
for here in range(1, N+1):
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

