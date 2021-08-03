from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijkstra(G, s):
    INF = 10**18
    dist = [INF] * len(G)
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, v = heappop(pq)
        if d > dist[v]:
            continue
        for u, weight in G[v]:
            nd = d + weight
            if dist[u] > nd:
                dist[u] = nd
                heappush(pq, (nd, u))
    return dist


def count_ways(G, dist, s):
    ways = [0] * len(G)
    ways[s] = 1
    visited = [False] * len(G)
    visited[s] = True
    pq = [(0, s)]
    while pq:
        d, v = heappop(pq)
        for u, d in G[v]:
            if dist[v] + d == dist[u]:
                ways[u] = (ways[u] + ways[v]) % mod
                if not visited[u]:
                    heappush(pq, (dist[u], u))
                    visited[u] = True
    return ways


mod = 10**9 + 7
N, M = list(map(int, input().split()))
S, T = list(map(int, input().split()))
S -= 1
T -= 1
G = [[] for _ in range(N)]
for _ in range(M):
    U, V, D = list(map(int, input().split()))
    U -= 1
    V -= 1
    G[U].append((V, D))
    G[V].append((U, D))
distS = dijkstra(G, S)
distT = dijkstra(G, T)
wayS = count_ways(G, distS, S)
wayT = count_ways(G, distT, T)
shortest = distS[T]
cnt = wayS[T]**2 % mod
if shortest % 2 == 0:
    for i in range(N):
        if distS[i] == distT[i] == shortest // 2:
            cnt = (cnt - (wayS[i] * wayT[i])**2) % mod
for i in range(N):
    for j, d in G[i]:
        if distS[i] + d + distT[j] == shortest:
            if distS[i] < distT[i] and distT[j] < distS[j]:
                cnt = (cnt - (wayS[i] * wayT[j])**2) % mod
print(cnt)
