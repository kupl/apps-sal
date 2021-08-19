import numpy as np
import sys
import heapq


def eccentricities(graph, vertices):
    ecc = []
    dist = floyd_warshall(graph, vertices)
    for u in dist:
        d = [dist[u][v] for v in dist[u] if dist[u][v] != INFINITY]
        if d:
            ecc.append(max(d))
    return ecc


def floyd_warshall(graph, vertices):
    dist = {}
    for u in vertices:
        dist[u] = {}
        for v in vertices:
            dist[u][v] = INFINITY
    for u in graph:
        dist[u][u] = 0
        for v in graph[u]:
            dist[u][v[0]] = v[1]
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


(n, e) = list(map(int, input().split()))
graph = {}
for _ in range(e):
    (u, v, w) = list(map(int, input().split()))
    u -= 1
    v -= 1
    if u in graph:
        graph[u] += [[v, w]]
    else:
        graph[u] = [[v, w]]
    if v in graph:
        graph[v] += [[u, w]]
    else:
        graph[v] = [[u, w]]
vertices = list(range(n))
INFINITY = 100000
ecc = eccentricities(graph, vertices)
radius = min(ecc)
diameter = max(ecc)
print(diameter)
