class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        out = 0
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges += [(abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j)]

        edges = sorted(edges, key=lambda x: x[0])

        p = [i for i in range(len(points))]

        def findparent(i):
            if i != p[i]:
                p[i] = findparent(p[i])
            return p[i]

        for e in edges:
            p1 = findparent(e[1])
            p2 = findparent(e[2])
            if p1 != p2:
                p[p2] = p1
                out += e[0]

        return out
