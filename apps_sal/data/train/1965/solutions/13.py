class DSU():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = n
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return False
        if self.rank[xp] < self.rank[yp]:
            self.parent[xp] = yp
        elif self.rank[xp] > self.rank[yp]:
            self.parent[yp] = xp
        else:
            self.parent[xp] = yp
            self.rank[yp] += 1
        self.size -= 1
        return True
    def getSize(self):
        return self.size
    
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n + 1)
        typeEdges = collections.defaultdict(list)
        for t, i, j in edges:
            typeEdges[t].append((i, j))
        res = 0
        for i, j in typeEdges[3]:
            if not dsu.union(i, j):
                res += 1
        if dsu.getSize() == 2:
            return res + sum(len(v) for k, v in typeEdges.items() if k in [1, 2])
        for i, j in typeEdges[1]:
            if not dsu.union(i, j):
                res += 1
        if dsu.getSize() > 2:
            return -1
        dsu1 = DSU(n + 1)
        for i, j in typeEdges[3]:
            dsu1.union(i, j)
        for i, j in typeEdges[2]:
            if not dsu1.union(i, j):
                res += 1
        if dsu1.getSize() > 2:
            return -1
        return res
