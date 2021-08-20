class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        (ans, n) = (0, len(points))
        seen = set()
        vertices = [(0, (0, 0))]
        while len(seen) < n:
            (w, (u, v)) = heapq.heappop(vertices)
            if v in seen:
                continue
            ans += w
            seen.add(v)
            for j in range(n):
                if j not in seen:
                    heapq.heappush(vertices, (manhattan(points[j], points[v]), (v, j)))
        return ans
