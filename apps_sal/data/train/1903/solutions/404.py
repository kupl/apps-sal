class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        points = [tuple(p) for p in points]
        (ans, n) = (0, len(points))
        seen = set()
        vertices = [(0, (points[0], points[0]))]
        while len(seen) < n:
            (w, (u, v)) = heapq.heappop(vertices)
            if u in seen and v in seen:
                continue
            ans += w
            seen.add(v)
            for (j, p) in enumerate(points):
                if tuple(p) != tuple(v) and tuple(p) not in seen:
                    heapq.heappush(vertices, (manhattan(p, v), (tuple(v), tuple(p))))
            seen.add(u)
        return ans
