class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhattan(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        (ans, n) = (0, len(points))
        seen = set()
        edges = [(0, 0, 0)]
        while len(seen) < n:
            (w, u, v) = heapq.heappop(edges)
            if v in seen:
                continue
            seen.add(v)
            ans += w
            for i in range(len(points)):
                if i not in seen and i != u:
                    heapq.heappush(edges, (manhattan(points[v], points[i]), v, i))
        return ans
