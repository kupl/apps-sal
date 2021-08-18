class Unifind:
    def __init__(self, n):
        self.arr = list(range(n))
        self.rank = [0] * n

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if self.rank[a] < self.rank[b]:
            a, b = b, a

        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1

        self.arr[b] = a

    def find(self, a):
        if self.arr[a] != a:
            self.arr[a] = self.find(self.arr[a])
        return self.arr[a]


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def manhatan(x1, y1, x2, y2): return (x1 - x2 if x1 > x2 else x2 - x1) + (y1 - y2 if y1 > y2 else y2 - y1)
        edges = [(manhatan(points[i][0], points[i][1], points[j][0], points[j][1]), i, j) for i in range(len(points)) for j in range(i + 1, len(points))]
        heapify(edges)
        uf = Unifind(len(points))
        count = 0
        cost = 0
        while count < len(points) - 1:
            c, i, j = heappop(edges)
            if uf.find(i) != uf.find(j):
                cost += c
                count += 1
                uf.union(i, j)

        return cost
