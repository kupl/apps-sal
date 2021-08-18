class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        hq = [(0, points[0][0], points[0][1])]
        seen = set()
        total = 0
        while hq:
            dist, x, y = heappop(hq)
            if (x, y) in seen:
                continue
            total += dist
            seen.add((x, y))
            for nx, ny in points:
                if (nx, ny) not in seen:
                    dist = abs(nx - x) + abs(ny - y)
                    heappush(hq, (dist, nx, ny))
        return total
