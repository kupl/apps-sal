class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n
        self.rank = [1] * n

    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])  # path compression
        return self.parent[p]

    def union(self, p, q):
        prt = self.find(p)
        qrt = self.find(q)
        if prt == qrt:
            return False  # already connected
        if self.rank[prt] > self.rank[qrt]:
            prt, qrt = qrt, prt
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)

        hp = []  # min heap

        for i in range(n):
            x, y = points[i]
            for ii in range(i + 1, n):
                xx, yy = points[ii]
                cost = abs(x - xx) + abs(y - yy)
                heappush(hp, (cost, i, ii))

        ans = 0
        while hp and uf.count != 1:
            cost, i, ii = heappop(hp)
            if uf.union(i, ii):
                ans += cost
        return ans
