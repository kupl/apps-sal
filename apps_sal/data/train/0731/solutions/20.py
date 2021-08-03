# cook your dish here
c, f = map(int, input().split())
dist = [[float('Inf') for _ in range(c)] for _ in range(c)]
for _ in range(f):
    u, v, p = map(int, input().split())
    u -= 1
    v -= 1
    dist[u][v] = p
    dist[v][u] = p
for i in range(c):
    dist[i][i] = 0
for k in range(c):
    for i in range(c):
        for j in range(c):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
massimo = 0
for i in range(c):
    massimo = max(massimo, max(dist[i]))
print(massimo)
