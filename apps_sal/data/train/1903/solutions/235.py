import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        res, n = 0, len(points)
        verticles = [(0, (0, 0))]
        visited = set()

        while len(visited) < n:
            d, (pre, cur) = heapq.heappop(verticles)
            if cur in visited:
                continue
            res += d
            visited.add(cur)
            for nxt in range(n):
                if nxt not in visited and nxt != cur:
                    heapq.heappush(verticles, (manhattan(points[cur], points[nxt]), (cur, nxt)))
        return res
