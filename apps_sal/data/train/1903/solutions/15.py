class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        costMap = [0] * len(points)

        minHeap = []
        heappush(minHeap, (0, points[0], 0))
        visited = set()

        while minHeap:
            cost, [currentX, currentY], currentIndex = heappop(minHeap)
            if (currentX, currentY) in visited:
                if costMap[currentIndex] <= cost:
                    continue

            for i, p in enumerate(points):
                if not ((p[0], p[1]) in visited) and i != currentIndex:
                    nextCost = abs(currentX - p[0]) + abs(currentY - p[1])
                    heappush(minHeap, (nextCost, p, i))
            if (currentX, currentY) in visited:
                costMap[currentIndex] = min(costMap[currentIndex], cost)
            else:
                costMap[currentIndex] = cost

            visited.add((currentX, currentY))

        return sum(costMap)
