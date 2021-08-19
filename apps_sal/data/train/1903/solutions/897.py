from heapq import heappush, heappop


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distsDict = [[None] * len(points) for _ in range(len(points))]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distsDict[i][j] = distsDict[j][i] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        q = [(0, 0)]
        visited = set()
        totalCost = 0
        while q:
            (cost, point) = heappop(q)
            if point not in visited:
                visited.add(point)
                totalCost += cost
                for i in range(len(points)):
                    if i != point and (not i in visited):
                        heappush(q, (distsDict[point][i], i))
        return totalCost
