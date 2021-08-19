from heapq import heappush, heappop
from collections import defaultdict


class Solution:
    """
    min-spanning-tree?
    * generate graph from all points
    * edgerelaxation with pq,
    """

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def taxicab(x1, x2, y1, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        def gengraph():
            graph = defaultdict(list)
            for (i, point) in enumerate(points):
                (x1, y1) = point
                for j in range(i + 1, len(points)):
                    (x2, y2) = points[j]
                    cost = taxicab(x1, x2, y1, y2)
                    graph[x1, y1].append((cost, (x2, y2)))
                    graph[x2, y2].append((cost, (x1, y1)))
            return graph
        graph = gengraph()
        relaxed = set()
        start = tuple(points[0])
        heap = [(0, start)]
        mincost = 0
        while heap and len(relaxed) < len(points):
            (cost, pos) = heappop(heap)
            if pos in relaxed:
                continue
            relaxed.add(pos)
            mincost += cost
            for nbr in graph[pos]:
                if nbr not in relaxed:
                    heappush(heap, nbr)
        return mincost
