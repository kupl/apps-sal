from heapq import heappush, heappop
from collections import defaultdict


def dijkstra(V, E, s):
    '''
    Input:
        V = list(range(N))
        E = defaultdict(dict)
        s (in V) : start vertex
    Output:
        dist: the list of the minimum cost from s to arbitrary vertex v in the given graph
    '''
    INF = float('inf')
    dist = {v: INF for v in V}
    heap = []
    dist[s] = 0
    rem = len(V)
    heappush(heap, (0, s))
    while heap and rem:
        d, v = heappop(heap)
        if d > dist[v]:
            continue
        rem -= 1
        for u, c in E[v].items():
            temp = d + c
            if temp < dist[u]:
                dist[u] = temp
                heappush(heap, (temp, u))
    return dist


N = int(input())
V = list(range(1, N + 1))
E = defaultdict(dict)
for _ in range(N - 1):
    a, b = map(int, input().split())
    E[a][b] = 1
    E[b][a] = 1
fen = dijkstra(V, E, 1)
sun = dijkstra(V, E, N)
black, white = 0, 0
for v in V:
    if fen[v] <= sun[v]:
        black += 1
    else:
        white += 1
print('Fennec' if black > white else 'Snuke')
