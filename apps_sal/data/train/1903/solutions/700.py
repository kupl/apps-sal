from heapq import heappush


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        minCost = 0
        minEdges = []
        heappush(minEdges, (0, 0))

        while(len(visited) < len(points)):

            vertexDistance, vertexIdx = heappop(minEdges)
            if vertexIdx in visited:
                continue
            print(vertexIdx)
            visited.add(vertexIdx)
            minCost += vertexDistance

            vertexX = points[vertexIdx][0]
            vertexY = points[vertexIdx][1]

            for adjIdx, adjPos in enumerate(points):
                if adjIdx not in visited:
                    adjX = points[adjIdx][0]
                    adjY = points[adjIdx][1]

                    distance = abs(vertexX - adjX) + abs(vertexY - adjY)
                    heappush(minEdges, (distance, adjIdx))

        return minCost
