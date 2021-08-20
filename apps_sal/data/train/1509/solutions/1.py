from bisect import insort


class disk:

    def __init__(self):
        self.U = ''
        self.D = ''
        self.L = ''
        self.R = ''


(m, n) = map(int, input().split())
adj = [[] for _ in range(m * n)]
grid = [[disk() for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        (grid[i][j].U, grid[i][j].R, grid[i][j].D, grid[i][j].L) = input().split()
for i in range(m):
    for j in range(n):
        if j != 0:
            if grid[i][j].R == grid[i][j - 1].R:
                dist = 2
            if grid[i][j].U == grid[i][j - 1].R:
                dist = 3
            if grid[i][j].L == grid[i][j - 1].R:
                dist = 0
            if grid[i][j].D == grid[i][j - 1].R:
                dist = 1
            adj[i * n + j].append((dist, i * n + j - 1))
        if j != n - 1:
            if grid[i][j].R == grid[i][j + 1].L:
                dist = 0
            if grid[i][j].U == grid[i][j + 1].L:
                dist = 1
            if grid[i][j].L == grid[i][j + 1].L:
                dist = 2
            if grid[i][j].D == grid[i][j + 1].L:
                dist = 3
            adj[i * n + j].append((dist, i * n + j + 1))
        if i != 0:
            if grid[i][j].R == grid[i - 1][j].D:
                dist = 3
            if grid[i][j].U == grid[i - 1][j].D:
                dist = 0
            if grid[i][j].L == grid[i - 1][j].D:
                dist = 1
            if grid[i][j].D == grid[i - 1][j].D:
                dist = 2
            adj[i * n + j].append((dist, i * n + j - n))
        if i != m - 1:
            if grid[i][j].R == grid[i + 1][j].U:
                dist = 1
            if grid[i][j].U == grid[i + 1][j].U:
                dist = 2
            if grid[i][j].L == grid[i + 1][j].U:
                dist = 3
            if grid[i][j].D == grid[i + 1][j].U:
                dist = 0
            adj[i * n + j].append((dist, i * n + j + n))
q = []
q.append((0, 0))
dists = [2147483647 for _ in range(m * n)]
visited = [False for _ in range(m * n)]
dists[0] = 0
while q:
    cur = q[-1]
    q.pop()
    if visited[cur[1]] == False:
        visited[cur[1]] = True
        dists[cur[1]] = -1 * cur[0]
    for i in range(len(adj[cur[1]])):
        to = adj[cur[1]][i][1]
        dis = adj[cur[1]][i][0]
        if not visited[to] and dists[cur[1]] + dis < dists[to]:
            insort(q, (-1 * (dists[cur[1]] + dis), to))
print(dists[m * n - 1])
