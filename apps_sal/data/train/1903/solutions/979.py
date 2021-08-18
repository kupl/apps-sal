class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq
        n = len(points)

        pq = [(0, 0)]
        seen = [False] * n
        totalCost = 0
        while pq:
            cost, currPoint = heapq.heappop(pq)
            if seen[currPoint]:
                continue
            seen[currPoint] = True
            totalCost += cost

            x1, y1 = points[currPoint]
            for i in range(n):
                if i != currPoint and not seen[i]:
                    x2, y2 = points[i]
                    d = abs(x2 - x1) + abs(y2 - y1)
                    heapq.heappush(pq, (d, i))
        return totalCost
