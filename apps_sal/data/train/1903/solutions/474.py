class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, i):
        if self.parent[i] == i:
            return i
        else:
            return self.find(self.parent[i])

    def union(self, i, j):
        x, y = self.find(i), self.find(j)

        rx, ry = self.rank[x], self.rank[y]

        if rx > ry:
            self.parent[y] = x

        elif rx < ry:
            self.parent[x] = y

        else:
            self.parent[y] = x
            self.rank[x] += 1


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

                edges.append((i, j, dist))

        edges.sort(key=lambda x: x[2])

        d = DSU(n)

        e = 0
        i = 0
        ret = 0

        while e < n - 1:
            if d.find(edges[i][0]) != d.find(edges[i][1]):
                ret += edges[i][2]
                d.union(edges[i][0], edges[i][1])
                e += 1

            i += 1

        return ret
