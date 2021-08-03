class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(x, y): return abs(x[0] - y[0]) + abs(x[1] - y[1])
        neighbors = collections.defaultdict(dict)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                neighbors[i][j] = dist(points[i], points[j])
                neighbors[j][i] = dist(points[i], points[j])
        pq = [(0, 0)]
        visited = set()
        res = 0
        while len(visited) < len(points):
            d, u = heapq.heappop(pq)
            if u in visited:
                continue
            print(d, u)
            res += d
            visited.add(u)
            for v, d_ in neighbors[u].items():
                heapq.heappush(pq, (d_, v))
        return res
