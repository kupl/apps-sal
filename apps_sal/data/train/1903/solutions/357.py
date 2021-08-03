class DSU:
    def __init__(self, size):
        self.par = list(range(size))

    def find(self, x):
        if self.par[x] != x:
            return self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(u, v):
            return abs(u[0] - v[0]) + abs(u[1] - v[1])
        points_dist = collections.defaultdict(dict)
        edges = []
        for i, p1 in enumerate(points):
            for j in range(i + 1, len(points)):
                points_dist[i][j] = distance(points[i], points[j])
                heapq.heappush(edges, (distance(points[i], points[j]), i, j))
        res = 0
        count = 0
        dsu = DSU(len(points))
        while count < len(points) - 1:
            distance, x, y = heapq.heappop(edges)
            p_x, p_y = dsu.find(x), dsu.find(y)
            if p_x != p_y:
                count += 1
                res += distance
                dsu.union(x, y)
        return res
