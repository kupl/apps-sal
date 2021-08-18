import heapq

xs, ys, xt, yt = list(map(int, input().split()))
N = int(input())
XYR = [list(map(int, input().split())) for i in range(N)]
XYR.append([xs, ys, 0])
XYR.append([xt, yt, 0])
L = [[9999999999] * (N + 2) for i in range(N + 2)]
for i in range(N + 2):
    for j in range(i, N + 2):
        x1, y1, r1 = XYR[i]
        x2, y2, r2 = XYR[j]
        L[i][j] = L[j][i] = max(((x1 - x2)**2 + (y1 - y2)**2)**0.5 - r1 - r2, 0.0)


num = N + 2
start = num - 2

distance = [float('inf') for i in range(num)]
prev = [float('inf') for i in range(num)]
distance[start] = 0
q = []
heapq.heappush(q, (0, start))

while len(q) != 0:
    prov_cost, src = heapq.heappop(q)

    if distance[src] < prov_cost:
        continue

    for destination, cost in enumerate(L[src]):
        if distance[destination] > distance[src] + cost:
            distance[destination] = distance[src] + cost
            heapq.heappush(q, (distance[destination], destination))
            prev[destination] = src

print((distance[-1]))
