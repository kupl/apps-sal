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
            x, y = y, x
        self.father[y] = x
        self.rank[x] += self.rank[y]
        self.count -= 1

    def find_union(self, x, y):
        father_x, father_y = self.find(x), self.find(y)
        if father_x != father_y:
            self.union(father_x, father_y)
            return True
        return False


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mst = collections.defaultdict(set)
        edges = []
        n = len(points)
        graph = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if i == j:
                    continue
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))
        uf = Union_Find(n)
        heapq.heapify(edges)
        result = 0
        while edges:
            cost, frm, to = heapq.heappop(edges)
            if uf.find_union(frm, to):
                result += cost
                print((frm, to))
        return result
