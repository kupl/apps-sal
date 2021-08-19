xs, ys, xe, ye = list(map(int, input().split()))
n = int(input())
xyr = [tuple(map(int, input().split())) for _ in range(n)]
xyr.append((xs, ys, 0))
xyr.append((xe, ye, 0))
d = [[0] * (n + 2) for _ in range(n + 2)]
for i in range(n + 1):
    for j in range(i + 1, n + 2):
        x, y, r = xyr[i]
        nx, ny, nr = xyr[j]
        tmp = ((x - nx)**2 + (y - ny)**2)**0.5
        tmp -= r + nr
        tmp = max(tmp, 0)
        d[i][j] = tmp
        d[j][i] = tmp


inf = float('inf')
seen = [inf] * (n + 2)
seen[-2] = 0
mi = set(range(n + 2))
# n->n+1
while mi:
    min_idx = 0
    min_d = inf
    for v in mi:
        if min_d > seen[v]:
            min_d = seen[v]
            min_idx = v
    v = min_idx
    mi.discard(v)
    if v == n + 1:
        break
    for nv in mi:
        seen[nv] = min(seen[nv], seen[v] + d[v][nv])
print((seen[-1]))
