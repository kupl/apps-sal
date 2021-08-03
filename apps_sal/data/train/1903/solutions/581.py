from heapq import heapify, heappush, heappop
from collections import defaultdict


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # helper function to calculate the manhatten distance
        # between two points
        def distance(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(points)
        if n == 1:
            return 0

        # convert all the points to tuples so they are hashable
        points = [tuple(p) for p in points]

        # build the graph
        # key: vertex
        # value: list of neighbors and their edge weights
        cost = defaultdict(list)
        for i in range(n):
            point1 = points[i]
            for j in range(i + 1, n):
                point2 = points[j]
                d = distance(point1, point2)
                cost[point1].append((d, point2))
                cost[point2].append((d, point1))

        ans = 0
        # we start at the first point in the input
        visited = {points[0]}
        # add all the neighbors of point 0 to PQ
        heap = cost[points[0]]
        heapify(heap)

        # we loop until all the points have been visited
        while len(visited) != n:
            # remove the vertex with the smallest edge weight
            d, v = heappop(heap)
            # check if this vertex is unvisited
            if v not in visited:
                # move this vertex to the visited set
                visited.add(v)
                # this edge is part of the MST
                ans += d
                # add all the neighbors of v into priority queue
                for record in cost[v]:
                    heappush(heap, record)

        return ans
