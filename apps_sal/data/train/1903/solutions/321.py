class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [[0] * n for _ in range(n)]
        res = 0
        for i in range(n):
            p = points[i]
            for j in range(n):
                nei = points[j]
                dist[i][j] = abs(p[0] - nei[0]) + abs(p[1] - nei[1])
        res = self.prim(n, dist, 0)
        return res

    def prim(self, n, dist, start):
        visited = set()
        res = 0
        nei = [[0, 0, 0]]
        heapq.heapify(nei)
        while len(visited) != n:
            (weight, current, dummy) = heapq.heappop(nei)
            if current in visited:
                continue
            res += weight
            visited.add(current)
            for i in range(n):
                if i not in visited:
                    heapq.heappush(nei, [dist[current][i], i, i])
        return res
