class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False

        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx
        self.size[rx] += self.size[ry]

        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        edges = []
        res = 0

        for i in range(N):
            for j in range(i + 1, N):
                distance = abs(points[i][0] - points[j][0])
                distance += abs(points[i][1] - points[j][1])

                edges.append((distance, i, j))

        edges.sort()

        unionfind = UnionFind(N)

        for edge in edges:
            dis, i, j = edge
            if unionfind.union(i, j):
                res += dis

        return res
