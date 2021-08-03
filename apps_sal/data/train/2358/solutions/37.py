from heapq import heapify, heappop, heappush
xs, ys, xt, yt = map(int, input().split())
INF = float("inf")
N = int(input())
Z = []
for i in range(N):
    x, y, r = map(int, input().split())
    Z.append((x, y, r, i))  # x,y,r,ID
G = [[] for _ in range(N + 2)]
for i in range(N):
    dis = ((Z[i][0] - xs)**2 + (Z[i][1] - ys)**2)**0.5
    dis -= Z[i][2]
    dis = max(0, dis)
    G[0].append((dis, i + 1))
dis = ((xt - xs)**2 + (yt - ys)**2)**0.5
G[0].append((dis, N + 1))

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        dis = ((Z[i][0] - Z[j][0])**2 + (Z[i][1] - Z[j][1])**2)**0.5
        dis -= Z[i][2] + Z[j][2]
        dis = max(0, dis)
        G[i + 1].append((dis, j + 1))  # 1index
    dis = ((Z[i][0] - xt)**2 + (Z[i][1] - yt)**2)**0.5
    dis -= Z[i][2]
    dis = max(0, dis)
    G[i + 1].append((dis, N + 1))
# print(G)


def dijkstra_heap2(s, G):
    # S:start, V: node, E: Edge, G: Graph
    V = len(G)
    d = [INF for _ in range(V)]
    d[s] = 0
    PQ = []
    heappush(PQ, (0, s))

    while PQ:
        c, v = heappop(PQ)
        if d[v] < c:
            continue
        d[v] = c
        for cost, u in G[v]:
            if d[u] <= cost + d[v]:
                continue
            d[u] = cost + d[v]
            heappush(PQ, (d[u], u))

    return d


ret = dijkstra_heap2(0, G)
# print(ret)
ans = ret[N + 1]
print(ans)
