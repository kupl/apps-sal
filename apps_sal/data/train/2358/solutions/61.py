from heapq import heappop, heappush
(sx, sy, tx, ty) = list(map(int, input().split()))
n = int(input())
barriers = [tuple(map(int, input().split())) for _ in range(n)]
barriers.append((tx, ty, 0))
barriers.append((sx, sy, 0))
s = n + 1
t = n
q = [(0.0, s)]
visited = [False] * (n + 2)
while q:
    (cost, v) = heappop(q)
    if v == t:
        print(cost)
        break
    if visited[v]:
        continue
    visited[v] = True
    (vx, vy, vr) = barriers[v]
    for u in range(n + 1):
        if visited[u]:
            continue
        (ux, uy, ur) = barriers[u]
        new_cost = max(0, ((vx - ux) ** 2 + (vy - uy) ** 2) ** 0.5 - vr - ur)
        heappush(q, (cost + new_cost, u))
