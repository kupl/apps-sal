from heapq import heapify, heappop, heappush
import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))
S, T = list(map(int, input().split()))
Graph = [set() for i in range(N)]
Edge = []
mod = 10**9 + 7
inf = float("inf")
for i in range(M):
    a, b, c = list(map(int, input().split()))
    Graph[a - 1].add((c, b - 1))
    Graph[b - 1].add((c, a - 1))
    Edge.append((a - 1, b - 1, c))
    Edge.append((b - 1, a - 1, c))


def dijkstra(s, n, links):
    Visited = [False] * n
    cost = [inf] * n
    P = [0] * n
    P[s] = 1
    cost[s] = 0
    heap = [(0, s)]
    heapify(heap)
    while heap:
        hc, hp = heappop(heap)
        if Visited[hp]:
            continue
        Visited[hp] = True
        for c, p in links[hp]:
            if Visited[p]:
                continue
            if c + hc < cost[p]:
                cost[p] = c + hc
                P[p] = P[hp]
                heappush(heap, (cost[p], p))
            elif c + hc == cost[p]:
                P[p] = (P[p] + P[hp]) % mod
    return cost, P


def dp(s, n, links, d):
    Visited = [False] * n
    cost = [inf] * n
    P = [0] * n
    P[s] = 1
    cost[s] = 0
    heap = [(0, s)]
    heapify(heap)
    while heap:
        hc, hp = heappop(heap)
        if 2 * hc > d:
            break
        if Visited[hp]:
            continue
        Visited[hp] = True
        for c, p in links[hp]:
            if Visited[p]:
                continue
            if c + hc < cost[p]:
                cost[p] = c + hc
                P[p] = P[hp]
                heappush(heap, (cost[p], p))
            elif c + hc == cost[p]:
                P[p] = (P[p] + P[hp]) % mod
    return cost, P


cost_S, P_S = dijkstra(S - 1, N, Graph)
D = cost_S[T - 1]
cost_T, P_T = dp(T - 1, N, Graph, D)
Pat = P_S[T - 1]
ans = (Pat**2) % mod
for a, b, c in Edge:
    if cost_S[a] + cost_T[b] + c == D:
        if 2 * cost_S[a] < D and 2 * cost_T[b] < D:
            ans -= ((P_S[a] * P_T[b])**2) % mod
for i in range(N):
    if 2 * cost_S[i] == 2 * cost_T[i] == D:
        ans -= ((P_S[i] * P_T[i])**2) % mod
print((ans % mod))
