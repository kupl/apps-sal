import heapq


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def distance(x, y):
            dx = abs(x[0] - y[0])
            dy = abs(x[1] - y[1])
            return dx + dy
        n = len(points)
        if n == 1:
            return 0
        if n == 2:
            return distance(points[0], points[1])
        cost = 0
        curr = 0
        dist = [float('inf')] * n
        explored = set()
        explored.add(0)
        cnt = 1
        while cnt < n:
            x = points[curr]
            for (j, y) in enumerate(points):
                if j in explored:
                    continue
                else:
                    dist[j] = min(dist[j], distance(x, y))
            (min_d, curr) = min(((d, j) for (j, d) in enumerate(dist)))
            explored.add(curr)
            cnt += 1
            dist[curr] = float('inf')
            cost += min_d
        return cost
