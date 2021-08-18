from heapq import heappop, heappush, heapify
from collections import defaultdict


def distance(pointA, pointB):

    return abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)

        mat = [[float('inf')] * n for i in range(n)]

        lookup = defaultdict(list)
        minHeap = []

        for idx, aPoint in enumerate(points):
            for bIdx in range(idx + 1, n):
                bPoint = points[bIdx]

                dist = distance(aPoint, bPoint)

                minHeap.append(dist)

                lookup[dist].append([idx, bIdx])

        if n == 1:
            return 0

        visited = set()
        cost = 0

        minHeap = sorted(minHeap)
        minValue = minHeap[0]
        minIndex = lookup[minValue][0]
        visited.add(minIndex[0])
        visited.add(minIndex[1])
        cost += minValue

        while len(visited) != n:
            for minValue in minHeap:
                minIndexs = lookup[minValue]
                ifFound = False

                for minIndex in minIndexs:
                    x = minIndex[0]
                    y = minIndex[1]
                    if x in visited and y in visited:
                        continue
                    elif x in visited or y in visited:
                        visited.add(x)
                        visited.add(y)
                        cost += minValue
                        ifFound = True
                        break
                if ifFound:
                    break

        return cost
