from heapq import *


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        d = collections.defaultdict(list)

        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                x = tuple(points[i])
                y = tuple(points[j])
                distance = abs(x[0] - y[0]) + abs(x[1] - y[1])
                d[x].append((distance, y))
                d[y].append((distance, x))

        start = tuple(points[0])
        heap = d[start].copy()
        heapify(heap)
        res, s = 0, set([start])
        while len(s) < n:
            closest = heappop(heap)
            while closest[1] in s:
                closest = heappop(heap)

            s.add(closest[1])
            res += closest[0]
            for neig in d[closest[1]]:
                if neig not in s:
                    heappush(heap, neig)

        return res
