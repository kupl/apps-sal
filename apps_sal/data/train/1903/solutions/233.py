import numpy as np


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        numNode = len(points)
        if numNode == 1:
            return 0
        totalCost = 0
        current = 0
        distance = [math.inf] * numNode
        explored = set()
        for i in range(numNode - 1):
            (x0, y0) = points[current]
            explored.add(current)
            for (j, (x, y)) in enumerate(points):
                if j in explored:
                    continue
                distance[j] = min(distance[j], abs(x0 - x) + abs(y0 - y))
            (cost, current) = min(((c, index) for (index, c) in enumerate(distance)))
            distance[current] = math.inf
            totalCost += cost
        return totalCost
