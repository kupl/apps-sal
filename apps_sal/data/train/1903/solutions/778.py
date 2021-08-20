class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        import heapq

        def find(x):
            if G[x] != x:
                G[x] = find(G[x])
            return G[x]

        def union(x, y):
            (x, y) = (find(x), find(y))
            if x == y:
                return False
            G[y] = x
            return True
        G = list(range(len(points)))
        HQ = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                (x1, y1) = points[i]
                (x2, y2) = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(HQ, (dist, i, j))
        res = 0
        while HQ:
            (d, i, j) = heapq.heappop(HQ)
            if union(i, j):
                res += d
        return res
