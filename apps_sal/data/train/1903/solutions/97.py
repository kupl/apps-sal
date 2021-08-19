from math import inf


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def dis(i, j):
            (x1, y1, x2, y2) = (points[i][0], points[i][1], points[j][0], points[j][1])
            ans = abs(x1 - x2) + abs(y1 - y2)
            return ans
        n = len(points)
        connected = set()
        connected.add(0)
        uncon = set()
        for i in range(1, n):
            uncon.add(i)
        edges = {}
        for i in range(n):
            for j in range(n):
                if i != j:
                    edges[i, j] = dis(i, j)
                    edges[j, i] = edges[i, j]
        total = 0
        dis = [inf for _ in range(n)]
        pt = 0
        for _ in range(n - 1):
            for i in uncon:
                dis[i] = min(edges[i, pt], dis[i])
            (score, pt) = min(((score, i) for (i, score) in enumerate(dis)))
            dis[pt] = inf
            total += score
            connected.add(pt)
            uncon.remove(pt)
        return total
