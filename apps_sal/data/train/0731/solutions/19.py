MAX = 10 ** 9
(c, f) = map(int, input().split())
g = []
for i in range(c):
    g.append([-1 for j in range(c)])
for i in range(f):
    (x, y, p) = map(int, input().split())
    g[x - 1][y - 1] = p
    g[y - 1][x - 1] = p
for i in range(c):
    for j in range(c):
        if i == j:
            g[i][j] = 0
        elif g[i][j] == -1:
            g[i][j] = MAX
for k in range(c):
    for i in range(c):
        for j in range(c):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])
p = 0
for i in range(c):
    for j in range(c):
        p = max(g[i][j], p)
print(p)
