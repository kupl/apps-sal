class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi != pj:
            self.parent[max(pi, pj)] = min(pi, pj)
            self.size[min(pi, pj)] += self.size[max(pi, pj)]
            self.size[max(pi, pj)] = 0


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        distances = []
        for idx0 in range(n):
            i0, j0 = points[idx0]
            for idx1 in range(idx0 + 1, n):
                i1, j1 = points[idx1]
                dis = abs(i0 - i1) + abs(j0 - j1)
                distances.append([dis, idx0, idx1])
        heapq.heapify(distances)

        res = 0
        uf = UnionFind(n)
        while uf.size[0] < n:
            dis, idx0, idx1 = heapq.heappop(distances)
            if uf.find(idx0) != uf.find(idx1):
                res += dis
                uf.union(idx0, idx1)
        return res
