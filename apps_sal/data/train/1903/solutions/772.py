from heapq import *


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def get_distance(p1, p2):
            return abs(p2[1] - p1[1]) + abs(p2[0] - p1[0])

        edges = []

        for i in range(0, len(points)):
            for j in range(i + 1, len(points)):

                heappush(edges, (get_distance(points[i], points[j]), i, j))

        parents = [i for i in range(len(points))]

        def find(point):
            nonlocal parents
            if parents[point] != point:
                parents[point] = find(parents[point])
            return parents[point]

        def union(x, y):
            nonlocal parents
            parents[find(x)] = find(y)

        cost = 0
        while edges:
            dist, p1, p2 = heappop(edges)
            if find(p1) != find(p2):
                union(p1, p2)
                cost += dist

        return cost
