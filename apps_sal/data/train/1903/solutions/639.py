class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def get_dist(p1, p2):
            (x1, y1) = p1
            (x2, y2) = p2
            return abs(x1 - x2) + abs(y1 - y2)
        N = len(points)
        res = 0
        minheap = [(0, 0)]
        seen = set()
        while minheap:
            (dist, p) = heapq.heappop(minheap)
            if p in seen:
                continue
            res += dist
            seen.add(p)
            for i in range(N):
                if i not in seen:
                    heapq.heappush(minheap, (get_dist(points[p], points[i]), i))
        return res
