from math import sqrt
from heapq import *


def dijkstra(graph, initial):
    ''' Dijkstra's shortest path algorithm. '''
    visited = {initial: 0}
    h, path = [(0, initial)], {}
    nodes = set(graph.keys())

    while nodes and h:
        current_weight, min_node = heappop(h)
        while h and (min_node not in nodes):
            current_weight, min_node = heappop(h)
        if not h and (min_node not in nodes):
            break

        nodes.remove(min_node)
        for v, w in graph[min_node]:
            weight = w + current_weight  # weight update step
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                heappush(h, (weight, v))
                path[v] = min_node
    return visited, path


xstart, ystart, xtarget, ytarget = map(int, input().split())
N = int(input())
circs = [tuple(map(int, input().split())) for _ in range(N)]

graph = {i: [] for i in range(N + 2)}


for i in range(N):
    xi, yi, ri = circs[i]
    for j in range(i):
        xj, yj, rj = circs[j]
        d = max(sqrt((xi - xj)**2 + (yi - yj)**2) - ri - rj, 0)
        graph[i].append((j, d))
        graph[j].append((i, d))

    # start
    dst = max(sqrt((xi - xstart)**2 + (yi - ystart)**2) - ri, 0)
    graph[i].append((N, dst))
    graph[N].append((i, dst))

    dtgt = max(sqrt((xi - xtarget)**2 + (yi - ytarget)**2) - ri, 0)
    graph[i].append((N + 1, dtgt))
    graph[N + 1].append((i, dtgt))

dsrctgt = sqrt((xstart - xtarget)**2 + (ystart - ytarget)**2)
graph[N].append((N + 1, dsrctgt))
graph[N + 1].append((N, dsrctgt))

visited, _ = dijkstra(graph, N)
print(visited[N + 1])
