from collections import deque

def dfs(graph, start, goal):
    s_stack = deque()
    g_stack = deque()
    visited = [0 for i in range(N+1)]
    s_stack.append([start,0])
    g_stack.append([goal, 0])
    visited[start] = 1 
    visited[goal] = 1 
    s_cnt = 1
    g_cnt = 1
    round = 0
    while s_stack or g_stack:
        while s_stack:
            a,cost = s_stack.popleft()
            if cost > round:
                s_stack.appendleft([a,cost])
                break
            for b in graph[a].keys():
                if not visited[b]:
                    s_stack.append([b,cost+1])
                    visited[b] += 1 
                    s_cnt += 1
        while g_stack:
            a, cost = g_stack.popleft()
            if cost > round:
                g_stack.appendleft([a,cost])
                break
            for b in graph[a].keys():
                if not visited[b]:
                    g_stack.append([b,cost+1])
                    visited[b] += 1 
                    g_cnt += 1
        round += 1
    # print(s_cnt, g_cnt)
    return s_cnt > g_cnt

N = int(input())
graph = {}
for i in range(N-1):
    a,b = map(int, input().split())
    if a not in graph:
        graph[a] = {}
    if b not in graph:
        graph[b] = {}
    graph[a][b] = graph[b][a] = 1
print('Fennec' if dfs(graph,1,N) else 'Snuke')
