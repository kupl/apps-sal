class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        h = []
        visited = set()

        def dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        for i in range(len(points)):
            for j in range(i):
                h.append((dist(points[i], points[j]), i, j))
        heapq.heapify(h)
        total = 0
        uf = UnionFind([i for i in range(len(points))])
        while h and len(visited) < len(points):
            (dist, i, j) = heapq.heappop(h)
            if uf.find(i) != uf.find(j):
                uf.union(i, j)
                total += dist
        return total


class UnionFind:

    def __init__(self, arr):
        self.parent = [i for i in range(len(arr))]
        self.rank = [0] * len(arr)

    def find(self, i):
        if self.parent[i] == i:
            return i
        p = self.find(self.parent[i])
        self.parent[i] = p
        return p

    def union(self, a, b):
        (pa, pb) = (self.find(a), self.find(b))
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        elif self.rank[pb] > self.rank[pa]:
            self.parent[pa] = pb
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1
