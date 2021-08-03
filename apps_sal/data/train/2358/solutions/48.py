from heapq import *

sx, sy, tx, ty = list(map(int, input().split()))
N = int(input())
circles = [tuple(map(int, input().split())) for _ in range(N)]

s = N
t = N + 1
adj_matrix = [[0] * (N + 2) for _ in range(N + 2)]
adj_matrix[s][t] = adj_matrix[t][s] = ((tx - sx)**2 + (ty - sy)**2) ** 0.5
for v, (x, y, r) in enumerate(circles):
    adj_matrix[s][v] = adj_matrix[v][s] = max(0, ((x - sx)**2 + (y - sy)**2) ** 0.5 - r)
    adj_matrix[t][v] = adj_matrix[v][t] = max(0, ((x - tx)**2 + (y - ty)**2) ** 0.5 - r)

for v1, (x1, y1, r1) in enumerate(circles):
    for v2, (x2, y2, r2) in enumerate(circles[v1 + 1:], start=v1 + 1):
        adj_matrix[v1][v2] = adj_matrix[v2][v1] = max(0, (((x1 - x2)**2 + (y1 - y2)**2)**0.5 - r1 - r2))

dp = [float('inf')] * (N + 2)
dp[t] = 0
pq = [(0, t)]
while pq:
    cost, v = heappop(pq)
    if dp[v] < cost:
        continue
    for nv, dist in enumerate(adj_matrix[v]):
        if dp[nv] > cost + dist:
            dp[nv] = cost + dist
            heappush(pq, (dp[nv], nv))

# print(dp)
print((dp[s]))
