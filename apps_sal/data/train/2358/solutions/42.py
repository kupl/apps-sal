import heapq

xs, ys, xt, yt = list(map(int, input().split()))
N = int(input())
XYR = [(xs, ys, 0), (xt, yt, 0)]
for _ in range(N):
    XYR.append(tuple(map(int, input().split())))

D = [[0] * (N + 2) for _ in range(N + 2)]
for i, (xi, yi, ri) in enumerate(XYR):
    for j, (xj, yj, rj) in enumerate(XYR[:i]):
        dx = xj - xi
        dy = yj - yi
        d = (dx * dx + dy * dy)**0.5
        D[i][j] = D[j][i] = max(0, d - ri - rj)

Q = [(0, 0)]
dist = [-1] * (N + 2)
nvisited = 0
while nvisited < N + 2:
    d, n = heapq.heappop(Q)
    if dist[n] != -1:
        continue
    dist[n] = d
    nvisited += 1

    for e, d_ne in enumerate(D[n]):
        if dist[e] == -1:
            heapq.heappush(Q, (d + d_ne, e))

print((dist[1]))
