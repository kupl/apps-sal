from math import sqrt
(xs, ys, xt, yt) = map(int, input().split())
n = int(input())
xyr = [list(map(int, input().split())) for i in range(n)]
xyr.insert(0, [xs, ys, 0])
xyr.append([xt, yt, 0])
Graph = [[0] * (n + 2) for i in range(n + 2)]
for i in range(n + 2):
    for j in range(n + 2):
        Graph[i][j] = max(0, sqrt((xyr[i][0] - xyr[j][0]) ** 2 + (xyr[i][1] - xyr[j][1]) ** 2) - (xyr[i][2] + xyr[j][2]))
INF = 10 ** 18
dist = [INF] * (n + 2)
visited = [False] * (n + 2)
dist[0] = 0
while True:
    v = -1
    for i in range(n + 2):
        if not visited[i] and (v == -1 or dist[i] < dist[v]):
            v = i
    if v == -1:
        break
    visited[v] = True
    for i in range(n + 2):
        dist[i] = min(dist[i], dist[v] + Graph[v][i])
print(dist[-1])
