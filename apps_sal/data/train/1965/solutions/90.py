class UF:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def isConnected(self, a, b):
        return self.find(a) == self.find(b)

    def find(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def union(self, a, b):
        p1 = self.find(a)
        p2 = self.find(b)
        if self.isConnected(p1, p2):
            return
        if self.size[p1] < self.size[p2]:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]
        else:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_1 = UF(n)
        uf_2 = UF(n)
        res = 0
        edges = sorted(edges, key=lambda edges: edges[0], reverse=True)
        for (t, a, b) in edges:
            if t == 3:
                if uf_1.isConnected(a - 1, b - 1) and uf_2.isConnected(a - 1, b - 1):
                    res += 1
                else:
                    uf_1.union(a - 1, b - 1)
                    uf_2.union(a - 1, b - 1)
            elif t == 1:
                if uf_1.isConnected(a - 1, b - 1):
                    res += 1
                else:
                    uf_1.union(a - 1, b - 1)
            elif uf_2.isConnected(a - 1, b - 1):
                res += 1
            else:
                uf_2.union(a - 1, b - 1)
        return res if self.isValid(uf_1, n) and self.isValid(uf_2, n) else -1

    def isValid(self, uf, n):
        for i in range(0, n - 1):
            if not uf.isConnected(i, i + 1):
                return False
        return True
