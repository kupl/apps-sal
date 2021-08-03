class uf(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if self.rank[p1] == self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += 1
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
        return

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        union_find = uf(len(points))
        ans = 0
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1]), i, j))

        edges = sorted(edges)
        for w, u, v in edges:
            if union_find.find(u) != union_find.find(v):
                union_find.union(u, v)
                ans += w
        return ans
