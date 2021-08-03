class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def getCost(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        res, N = 0, len(points)
        seen = set()
        vertices = [(0, (0, 0))]

        while len(seen) < N:
            w, (u, v) = heapq.heappop(vertices)
            if v in seen:
                continue
            res += w
            seen.add(v)
            for j in range(N):
                if j not in seen and j != v:
                    heapq.heappush(vertices, (getCost(points[v], points[j]), (v, j)))
        return res
