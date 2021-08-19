import heapq
(xs, ys, xt, yt) = list(map(int, input().split()))
n = int(input())
v = [(xs, ys, 0), (xt, yt, 0)]
for i in range(n):
    (x, y, r) = list(map(int, input().split()))
    v.append((x, y, r))
path = [[] for i in range(n + 2)]
for i in range(n + 1):
    for j in range(i + 1, n + 2):
        l = max(0, ((v[i][0] - v[j][0]) ** 2 + (v[i][1] - v[j][1]) ** 2) ** 0.5 - v[i][2] - v[j][2])
        path[i].append((j, l))
        path[j].append((i, l))


def Dijkstra(edge, start, v):
    d = [float('inf')] * v
    d[start] = 0
    pq = [(0, start)]
    heapq.heapify(pq)
    while pq:
        (dist, p) = heapq.heappop(pq)
        if dist > d[p]:
            continue
        for (to, cost) in edge[p]:
            if d[to] <= dist + cost:
                continue
            d[to] = dist + cost
            heapq.heappush(pq, (d[to], to))
    return d


d = Dijkstra(path, 0, n + 2)
print(d[1])
