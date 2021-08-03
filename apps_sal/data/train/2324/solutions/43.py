from collections import deque


def dfs(graph, start):
    stack = deque()
    costs = [0] * (N + 1)
    stack.append([start, 0])
    costs[start] = -1
    while stack:
        a, cost = stack.popleft()
        for b in list(graph[a].keys()):
            if not costs[b]:
                stack.append([b, cost + 1])
                costs[b] = cost + 1
    return costs


N = int(input())
graph = {}
for i in range(N - 1):
    a, b = list(map(int, input().split()))
    if a not in graph:
        graph[a] = {}
    if b not in graph:
        graph[b] = {}
    graph[a][b] = graph[b][a] = 1
f_costs = dfs(graph, 1)
s_costs = dfs(graph, N)
f_cnt = 1
for i in range(2, N):
    if f_costs[i] <= s_costs[i]:
        f_cnt += 1
# print(f_costs, s_costs, f_cnt)
print(('Fennec' if f_cnt > N - f_cnt else 'Snuke'))
