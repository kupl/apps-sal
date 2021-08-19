from heapq import heapify, heappop, heappush


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def getDistance(id1, id2):
            (x1, y1) = points[id1]
            (x2, y2) = points[id2]
            return abs(x1 - x2) + abs(y1 - y2)
        d = {}
        i = 0
        for (x, y) in points:
            d[x, y] = i
            i += 1
        n = i
        parent = [j for j in range(n)]

        def getId(x, y):
            return d[x, y]

        def find(id):
            if id != parent[id]:
                parent[id] = find(parent[id])
            return parent[id]

        def union(id1, id2):
            r1 = find(id1)
            r2 = find(id2)
            parent[r1] = r2
        edges = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    edges.append((i, j, getDistance(i, j)))
        edges.sort(key=lambda x: x[2])
        res = 0
        for edge in edges:
            if find(edge[0]) != find(edge[1]):
                res += edge[2]
                union(edge[0], edge[1])
        return res
