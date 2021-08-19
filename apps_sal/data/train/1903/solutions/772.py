from heapq import *


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def get_distance(p1, p2):
            return abs(p2[1] - p1[1]) + abs(p2[0] - p1[0])

        # edges
        edges = []

        for i in range(0, len(points)):
            for j in range(i + 1, len(points)):
                # edge = (distance, idx of point 1, idx of point 2)

                # sort edges
                heappush(edges, (get_distance(points[i], points[j]), i, j))

        # store all the parents for each point
        parents = [i for i in range(len(points))]

        # find the original parent of this element i.e. if its part of the currently beimg built MST
        def find(point):
            nonlocal parents
            if parents[point] != point:
                parents[point] = find(parents[point])
            return parents[point]

        # add a new point to the union
        def union(x, y):
            nonlocal parents
            parents[find(x)] = find(y)

        cost = 0
        while edges:
            dist, p1, p2 = heappop(edges)
            # if p1 and p2 aren't part of the same set, add p2 to the set.
            if find(p1) != find(p2):
                union(p1, p2)
                cost += dist

        return cost
