from heapq import heappush, heappop

sX, sY, tX, tY = list(map(int, input().split()))
N = int(input())

XYR = [tuple(map(int, input().split())) for _ in range(N)] + [(sX, sY, 0), (tX, tY, 0)]
S, T = N, N + 1
N += 2

edges = [[] for _ in range(N)]
for i, (x, y, r) in enumerate(XYR):
    for j, (u, v, w) in enumerate(XYR[i + 1:], start=i + 1):
        dist = max(0, ((x - u)**2 + (y - v)**2)**0.5 - (r + w))
        edges[i].append((j, dist))
        edges[j].append((i, dist))

minDist = [10**18] * N
minDist[S] = 0
que = [(0, S)]
while que:
    dist, now = heappop(que)
    if minDist[now] < dist:
        continue
    for to, cost in edges[now]:
        d = dist + cost
        if minDist[to] > d:
            minDist[to] = d
            heappush(que, (d, to))
print((minDist[T]))
