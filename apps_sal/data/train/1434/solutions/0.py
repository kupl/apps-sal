import numpy as np
(n, s, q) = [int(j) for j in input().split()]
edges = [int(j) - 1 for j in input().split()]
costs = [int(j) for j in input().split()]
special = [int(j) - 1 for j in input().split()]
queries = [[0] * 3 for _ in range(q)]
for i in range(q):
    queries[i] = [int(j) - 1 for j in input().split()]
edge_set = [[] for _ in range(n)]
for i in range(n - 1):
    edge_set[i + 1].append(edges[i])
    edge_set[edges[i]].append(i + 1)
stored = np.zeros((s, n, 1001), dtype=bool)
visited = [[] for _ in range(s)]
for i in range(s):
    s_vertex = special[i]
    s_cost = costs[s_vertex]
    s_visited = visited[i]
    s_visited.append(s_vertex)
    s_stored = stored[i]
    s_stored[s_vertex][0] = True
    s_stored[s_vertex][s_cost] = True
    for edge in edge_set[s_vertex]:
        s_visited.append(edge)
        s_stored[edge] = np.array(s_stored[s_vertex])
    for j in range(1, n):
        vertex = s_visited[j]
        cost = costs[vertex]
        s_stored[vertex][cost:1001] = np.logical_or(s_stored[vertex][0:1001 - cost], s_stored[vertex][cost:1001])
        for edge in edge_set[vertex]:
            if edge not in s_visited:
                s_visited.append(edge)
                s_stored[edge] = np.array(s_stored[vertex])
for i in range(q):
    (first, second, max_cost) = queries[i]
    bool_array = np.zeros(max_cost + 2, dtype=bool)
    for j in range(s):
        bool_array = np.logical_or(bool_array, np.logical_and(stored[j][first][:max_cost + 2], stored[j][second][:max_cost + 2]))
    for j in range(max_cost + 1, -1, -1):
        if bool_array[j]:
            print(2 * j)
            break
