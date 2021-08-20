import sys
from heapq import heappop, heappush


def I():
    return int(sys.stdin.readline().rstrip())


def MI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


(xs, ys, xt, yt) = MI()
N = I()
XYR = []
for _ in range(N):
    XYR.append(tuple(MI()))
XYR.append((xs, ys, 0))
XYR.append((xt, yt, 0))
Graph = [[0] * (N + 2) for _ in range(N + 2)]
for i in range(N + 1):
    (x0, y0, r0) = XYR[i]
    for j in range(i + 1, N + 2):
        (x1, y1, r1) = XYR[j]
        Graph[i][j] = max(0, ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5 - r0 - r1)
        Graph[j][i] = max(0, ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5 - r0 - r1)
dist = [10 ** 10] * (N + 2)
dist[N] = 0
q = []
heappush(q, (0, N))
flag = [0] * (N + 2)
while q:
    (d, i) = heappop(q)
    if flag[i] == 1:
        continue
    flag[i] = 1
    for j in range(N + 2):
        if flag[j] == 0:
            new_d = d + Graph[i][j]
            if new_d < dist[j]:
                dist[j] = new_d
                heappush(q, (new_d, j))
print(dist[N + 1])
