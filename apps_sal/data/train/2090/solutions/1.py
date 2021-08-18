import sys
from collections import deque

n, m = [int(i) for i in sys.stdin.readline().split()]
neighbors = [set() for _ in range(n)]
for i in range(m):
    m1, m2 = [int(i) for i in sys.stdin.readline().split()]
    neighbors[m1 - 1].add(m2 - 1)
    neighbors[m2 - 1].add(m1 - 1)

s1, t1, l1 = [int(i) for i in sys.stdin.readline().split()]
s2, t2, l2 = [int(i) for i in sys.stdin.readline().split()]
s1 -= 1
s2 -= 1
t1 -= 1
t2 -= 1

dists = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    q = deque([(i, 0)])
    visited = [False for _ in range(n)]
    visited[i] = True
    while len(q) != 0:
        v, dist = q.popleft()
        dists[i][v] = dist
        for neighbor in neighbors[v]:
            if not visited[neighbor]:
                q.append((neighbor, dist + 1))
                visited[neighbor] = True

best_found = m + 1
if dists[s1][t1] <= l1 and dists[s2][t2] <= l2:
    best_found = min(best_found, dists[s1][t1] + dists[s2][t2])

for u in range(n):
    for v in range(n):
        if u == v:
            continue
        path1_length = dists[s1][u] + dists[u][v] + dists[v][t1]
        path2_length = dists[s2][u] + dists[u][v] + dists[v][t2]
        if path1_length <= l1 and path2_length <= l2:
            total_length = path1_length + path2_length - dists[u][v]
            best_found = min(best_found, total_length)
        path1_length = dists[s1][u] + dists[u][v] + dists[v][t1]
        path2_length = dists[s2][v] + dists[v][u] + dists[u][t2]
        if path1_length <= l1 and path2_length <= l2:
            total_length = path1_length + path2_length - dists[u][v]
            best_found = min(best_found, total_length)
        path1_length = dists[s1][v] + dists[v][u] + dists[u][t1]
        path2_length = dists[s2][u] + dists[u][v] + dists[v][t2]
        if path1_length <= l1 and path2_length <= l2:
            total_length = path1_length + path2_length - dists[u][v]
            best_found = min(best_found, total_length)
        path1_length = dists[s1][v] + dists[v][u] + dists[u][t1]
        path2_length = dists[s2][v] + dists[v][u] + dists[u][t2]
        if path1_length <= l1 and path2_length <= l2:
            total_length = path1_length + path2_length - dists[u][v]
            best_found = min(best_found, total_length)

print(m - best_found)
