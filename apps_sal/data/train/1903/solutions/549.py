class UF(object):

    def __init__(self, size):
        # initially, each node is an independent component
        self.parent = [i for i in range(size)]
        # keep the size of each component
        self.size = [1] * (size)
        # count of the disconnected sets

    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootq == rootp:
            return
        if self.size[rootp] > self.size[rootq]:
            self.parent[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        else:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]

    def connected(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        return rootp == rootq

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        distances = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                distances.append((distance, i, j))
        distances.sort()
        uf = UF(len(points))
        res = 0
        for dis, u, v in distances:
            if not uf.connected(u, v):
                uf.union(u, v)
                res += dis
        return res
