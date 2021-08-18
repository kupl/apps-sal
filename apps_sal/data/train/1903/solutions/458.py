class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, a):
        if self.parent[a] == a:
            return a

        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        pa, pb = self.parent[a], self.parent[b]
        if pa == pb:
            return

        if self.rank[a] > self.rank[b]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]

        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def man_dist(a, b): return abs(a[0] - b[0]) + abs(a[1] - b[1])

        n = len(points)

        all_dists = []
        for i in range(n):
            for j in range(i + 1, n):
                all_dists.append((man_dist(points[i], points[j]), i, j))

        all_dists.sort(key=lambda x: x[0])

        ans = 0
        dis_set = DisjointSet(n)

        for dist, u, v in all_dists:
            if dis_set.find(u) != dis_set.find(v):
                dis_set.union(u, v)
                ans += dist

        return ans
