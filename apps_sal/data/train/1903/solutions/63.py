import heapq


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        (N, g) = (len(points), [])
        res = 0
        for i in range(N - 1):
            (x0, y0) = points[i]
            for j in range(i + 1, N):
                (x1, y1) = points[j]
                dist = abs(x0 - x1) + abs(y0 - y1)
                g.append((dist, (i, j)))
        heapq.heapify(g)
        parents = [None] * N
        for i in range(N):
            parents[i] = i

        def findParent(x):
            if parents[x] != x:
                parents[x] = findParent(parents[x])
            return parents[x]
        while g:
            (w, (a, b)) = heapq.heappop(g)
            pa = findParent(a)
            pb = findParent(b)
            if pa != pb:
                res += w
                parents[pa] = pb
        return res
