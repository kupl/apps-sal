import heapq as hq
(sx, sy, gx, gy) = list(map(int, input().split()))
N = int(input())
zone = [list(map(int, input().split())) for i in range(N)]
zone = [[sx, sy, 0]] + zone + [[gx, gy, 0]]
G = [[0] * (N + 2) for i in range(N + 2)]
for i in range(len(zone) - 1):
    for j in range(i + 1, len(zone)):
        dist = ((zone[i][0] - zone[j][0]) ** 2 + (zone[i][1] - zone[j][1]) ** 2) ** 0.5
        dist = max(0, dist - (zone[i][2] + zone[j][2]))
        G[i][j] = dist
        G[j][i] = dist
q = [(0, 0)]
hq.heapify(q)
seen = set()
while q:
    (dist, v) = hq.heappop(q)
    if v in seen:
        continue
    seen.add(v)
    if v == N + 1:
        print(dist)
        break
    for i in range(len(G[v])):
        if i in seen:
            continue
        hq.heappush(q, (dist + G[v][i], i))
