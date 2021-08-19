class Union_Find:

    def __init__(self, n):
        self.father = {i: i for i in range(n)}
        self.count = n
        self.rank = [1] * n

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, x, y):
        if self.rank[x] < self.rank[y]:
            (x, y) = (y, x)
        self.father[y] = x
        self.rank[x] += self.rank[y]
        self.count -= 1

    def find_union(self, x, y):
        (father_x, father_y) = (self.find(x), self.find(y))
        if father_x != father_y:
            self.union(father_x, father_y)
            return True
        return False


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mst = collections.defaultdict(set)
        n = len(points)
        graph = []
        uf = Union_Find(n)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                cost = cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph.append([i, j, cost])
        result = 0
        for (a, b, c) in sorted(graph, key=lambda x: x[2]):
            if uf.find_union(a, b):
                result += c
        return result
