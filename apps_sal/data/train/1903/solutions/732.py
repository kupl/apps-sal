class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        return True
    
class Solution:
    def minCostConnectPoints(self, points):
        N = len(points)
        
        edges = []
        for i in range(N):
            for j in range(i + 1, N):
                d = abs(points[i][0] - points[j][0])
                d += abs(points[i][1] - points[j][1])
                edges.append([d, i, j])
        edges.sort()

        ans = 0
        dsu = DSU(N)
        for d, u, v in edges:
            if dsu.union(u, v):
                ans += d
        return ans
    
        # n = len(points)
        # adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         adj_matrix[i][j] = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
        # visited = [False] * n
        # visited[0] = True
        # weight = [0] * n
        # for j in range(n):
        #     if j == 0:
        #         weight[j] = float('inf')
        #     else:
        #         weight[j] = adj_matrix[0][j]
        # total = 0
        # visit = 0
        # while not all(visited):
        #     visit = weight.index(min(weight))
        #     total += weight[visit]
        #     visited[visit] = True
        #     for j in range(n):
        #         if weight[j] == float('inf'):
        #             continue
        #         if j == visit:
        #             weight[j] = float('inf')
        #             continue
        #         weight[j] = min(weight[j], adj_matrix[visit][j])
        # return total

