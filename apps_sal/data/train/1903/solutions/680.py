class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parx, pary = self.find(x), self.find(y)
        if parx == pary:
            return False
        self.parent[pary] = parx
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append([distance(points[i], points[j]), i, j])
        edges.sort()

        dset = DisjointSet(len(points))
        res = numOfEdges = idx = 0
        while numOfEdges < len(points) - 1:
            w, u, v = edges[idx]
            if dset.union(u, v):
                res += w
                numOfEdges += 1
            idx += 1

        return res
