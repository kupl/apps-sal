import heapq
(xs, ys, xt, yt) = map(int, input().split())
N = int(input())
L = [[xs, ys, 0], [xt, yt, 0]]
for _ in range(N):
    L.append(list(map(int, input().split())))
V = N + 2
G = [[] for _ in range(N + 2)]
s = 0
for i in range(N + 2):
    for j in range(N + 2):
        if i != j:
            G[i].append([j, max(0, ((L[i][0] - L[j][0]) ** 2 + (L[i][1] - L[j][1]) ** 2) ** 0.5 - (L[i][2] + L[j][2]))])
INF = float('inf')


def dijkstra(s):
    d = [INF for _ in range(V)]
    d[s] = 0
    que = []
    heapq.heappush(que, (0, s))
    while len(que) != 0:
        p = heapq.heappop(que)
        v = p[1]
        if d[v] < p[0]:
            continue
        for i in range(len(G[v])):
            e = G[v][i]
            if d[e[0]] > d[v] + e[1]:
                d[e[0]] = d[v] + e[1]
                heapq.heappush(que, (d[e[0]], e[0]))
    return d


d = dijkstra(0)
print(d[1])
