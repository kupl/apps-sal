from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = 10**18
mod = 10**9 + 7


def dijkstra(start, n, graph):
    route_cnt = [start] * n
    route_cnt[start] = 1
    que = [(0, start)]
    dist = [INF] * n
    dist[start] = 0
    while que:
        min_dist, u = heappop(que)
        if min_dist > dist[u]:
            continue
        for c, v in graph[u]:
            if dist[u] + c < dist[v]:
                dist[v] = dist[u] + c
                route_cnt[v] = route_cnt[u]
                heappush(que, (dist[u] + c, v))
            elif dist[u] + c == dist[v]:
                route_cnt[v] = (route_cnt[v] + route_cnt[u]) % mod
    return route_cnt, dist


N, M = list(map(int, input().split()))
S, T = list(map(int, input().split()))
G = [[] for _ in range(N)]
edges = []
for _ in range(M):
    u, v, d = list(map(int, input().split()))
    G[u - 1].append((d, v - 1))
    G[v - 1].append((d, u - 1))
    edges.append((v - 1, u - 1, d))
num_s, dist_s = dijkstra(S - 1, N, G)
num_t, dist_t = dijkstra(T - 1, N, G)
ans = num_s[T - 1]**2 % mod
l = dist_s[T - 1]
for u, v, d in edges:
    if dist_s[v] < dist_s[u]:
        u, v = v, u
    if dist_s[u] * 2 < l < dist_s[v] * 2 and dist_s[u] + dist_t[v] + d == l:
        ans -= (num_s[u]**2 % mod) * (num_t[v]**2 % mod)
        ans %= mod
for v in range(N):
    if dist_s[v] == dist_t[v] == l / 2:
        ans -= (num_t[v]**2 % mod) * (num_s[v]**2 % mod)
        ans %= mod
print((ans % mod))
