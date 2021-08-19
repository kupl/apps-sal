# cook your dish here
# cook your dish here
t = int(input().strip())
result = []


class Distance:
    def __init__(self, n, dist):
        self.n = n
        self.dist = dist

    def cal_dist(self, u, v):
        self.dist[u][v] = self.dist[v][u] = 1
        for i in range(n):
            if self.dist[u][i] != -1 and self.dist[v][i] == -1 and i != u and i != v:
                self.dist[v][i] = self.dist[i][v] = self.dist[u][i] + 1
        for i in range(n):
            if self.dist[v][i] != -1 and self.dist[u][i] == -1 and i != u and i != v:
                self.dist[u][i] = self.dist[i][u] = self.dist[v][i] + 1

    def return_dist(self):
        return self.dist


for i in range(t):
    n, q = map(int, input().strip().split())
    dist = [[-1 for j in range(n)] for k in range(n)]
    for j in range(n):
        dist[j][j] = 0
    d = Distance(n, dist)
    for j in range(n - 1):
        u, v = map(int, input().strip().split())
        d.cal_dist(u - 1, v - 1)
    dist = d.return_dist()
    for j in range(q):
        a, da, b, db = map(int, input().strip().split())
        ans = -1
        for k in range(n):
            if dist[a - 1][k] == da and dist[b - 1][k] == db:
                ans = k + 1
                break
        result.append(ans)

print(*result, sep="\n")
