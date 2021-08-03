class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        npoints = len(points)
        if npoints == 1:
            return 0
        edges = dict()
        for i in range(npoints):
            for j in range(i + 1, npoints):
                edges[(i, j)] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        sortededges = {k: v for k, v in sorted(edges.items(), key=lambda item: item[1])}

        parent = [i for i in range(npoints)]
        mincost = 0
        numedges = 0
        for edge in sortededges:
            if self.findParent(parent, edge[0]) == self.findParent(parent, edge[1]):
                continue
            else:
                mincost += sortededges[edge]
                self.union(parent, edge[0], edge[1])
                numedges += 1
                if numedges == npoints - 1:
                    return mincost

    def findParent(self, parent, i):
        if parent[i] == i:
            return i
        return self.findParent(parent, parent[i])

    def union(self, parent, u, v):
        u_set = self.findParent(parent, u)
        v_set = self.findParent(parent, v)
        parent[u_set] = v_set
