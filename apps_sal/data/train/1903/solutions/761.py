class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        ans = 0
        h = []
        heappush(h, (0, points[0]))
        visited = set()
        while h:
            (d, p) = heappop(h)
            if (p[0], p[1]) in visited:
                continue
            visited.add((p[0], p[1]))
            ans += d
            for point in points:
                if (point[0], point[1]) not in visited:
                    heappush(h, (distance(p, point), point))
        return ans
