from heapq import *


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        adjList = self.buildAdjList(points)

        heap = [(0, 0, 0)]
        visited = set()
        minCost = 0
        while heap and len(visited) != len(adjList):
            cost, i, j = heappop(heap)
            if j in visited:
                continue

            visited.add(j)
            minCost += cost

            for nj, cost in adjList[j]:
                if nj not in visited:
                    heappush(heap, (cost, j, nj))
        return minCost

    def buildAdjList(self, points):
        adjList = {}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if i not in adjList:
                    adjList[i] = []
                if j not in adjList:
                    adjList[j] = []

                weight = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append((j, weight))
                adjList[j].append((i, weight))
        return adjList
