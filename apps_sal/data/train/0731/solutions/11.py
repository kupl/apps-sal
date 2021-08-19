import numpy as np
import sys
import heapq
# class Graph():

#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[0 for column in range(vertices)]
#                     for row in range(vertices)]

#     def minDistance(self, dist, sptSet, src):
#         min = sys.maxsize
#         min_index = -1
#         for v in range(self.V):
#             if dist[v] < min and sptSet[v] == False :
#                 min = dist[v]
#                 min_index = v

#         return min_index


#     def dijkstra(self, src):

#         # weights = self.graph[src]

#         # for i in range(self.V) :
#         #     self.graph[src][i] = 0
#         #     self.graph[i][src] = 0


#         dist = [sys.maxsize] * self.V
#         dist[src] = 0
#         sptSet = [False] * self.V

#         for cout in range(self.V):
#             u = self.minDistance(dist, sptSet, src)
#             if u == -1 : continue
#             sptSet[u] = True
#             for v in range(self.V):
#                 if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
#                     dist[v] = dist[u] + self.graph[u][v]


#         # for i in range(self.V) :
#         #     self.graph[src][i] = weights[i]
#         #     self.graph[i][src] = weights[i]

#         dist.remove(0)
#         MINIMUM = np.inf
#         for idx in range(len(dist)):
#             if idx != src and not self.graph[idx][src] and dist[idx] < MINIMUM :
#                 MINIMUM = dist[idx]

#         return MINIMUM

# def findCheapestPrice(n, flights, src , dst ) :
#     graph = {}

#     for u in range(n):
#         graph[u] = []

#     for u,v,w in flights:
#         graph[u].append((v,w))

#     heap = [(0,-n,src)]


#     while heap:
#         (cost,i,u) = heapq.heappop(heap)

#         if u == dst :
#             return cost
#             # if i >= n - 1 : continue
#             # else:  return cost
#             # if u not in list(zip(*graph[src]))[0] : return cost

#         for v,w in graph[u]:
#             nc = cost + w

#             if i <= 0:
#                 heapq.heappush(heap, (nc,i + 1,v))

#     return -1

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
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# MY SOLUTION = DIJKSTRA with at least 2 edges
n, e = list(map(int, input().split()))
graph = {}
for _ in range(e):
    u, v, w = list(map(int, input().split()))
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

INFINITY = 10**9
ecc = eccentricities(graph, vertices)
radius = min(ecc)
diameter = max(ecc)

print(diameter)
