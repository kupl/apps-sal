import sys
from heapq import heappush, heappop

input = sys.stdin.readline
xs, ys, xt, yt = map(int, input().split())
N = int(input())

x_list = []
y_list = []
r_list = []
x_list.append(xs)
y_list.append(ys)
r_list.append(0)
x_list.append(xt)
y_list.append(yt)
r_list.append(0)
for _ in range(N):
    x, y, r = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
    r_list.append(r)

edges = [[] for _ in range(N + 2)]
for i in range(N + 1):
    for j in range(i + 1, N + 2):
        x1, y1, r1 = x_list[i], y_list[i], r_list[i]
        x2, y2, r2 = x_list[j], y_list[j], r_list[j]
        d = max(0, ((x1 - x2)**2 + (y1 - y2)**2)**0.5 - r1 - r2)
        edges[i].append((j, d))
        edges[j].append((i, d))

INF = 10**10
dist = [INF] * (N + 2)
hq = [(0, 0)]
dist[0] = 0
while hq:
    cost, node = heappop(hq)
    if cost > dist[node]:
        continue
    for next, cost in edges[node]:
        if dist[node] + cost < dist[next]:
            dist[next] = dist[node] + cost
            heappush(hq, (dist[next], next))

print(dist[1])
