class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dists = []
        n = len(points)
        for i in range(n - 1):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dists.append((abs(x1 - x2) + abs(y1 - y2), i, j))

        roots = [-1] * n

        def find(p1):
            while roots[p1] >= 0:
                p1 = roots[p1]
            return p1

        def union(r1, r2):
            if roots[r1] < roots[r2]:
                roots[r1] += roots[r2]
                roots[r2] = r1
            else:
                roots[r2] += roots[r1]
                roots[r1] = r2

        # print(roots)
        #union(0, 3)
        # print(roots)

        res = 0
        heapq.heapify(dists)
        while dists:
            dist, p1, p2 = heapq.heappop(dists)
            r1 = find(p1)
            r2 = find(p2)
            if r1 != r2:
                union(r1, r2)
                res += dist

        return res
