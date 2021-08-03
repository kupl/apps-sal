class UnionFind:
    def __init__(self, N):
        self.par = [-1] * N
        self.N = N

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def groupCount(self):
        return len(self.roots())


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        uf1 = UnionFind(n)
        uf2 = UnionFind(n)
        ans = 0
        m = len(edges)
        for edge in edges:
            if edge[0] == 3:
                if uf.find(edge[1] - 1) == uf.find(edge[2] - 1):
                    ans += 1
                uf.union(edge[1] - 1, edge[2] - 1)
                uf1.union(edge[1] - 1, edge[2] - 1)
                uf2.union(edge[1] - 1, edge[2] - 1)
            elif edge[0] == 1:
                uf1.union(edge[1] - 1, edge[2] - 1)
                ans += 1
            else:
                uf2.union(edge[1] - 1, edge[2] - 1)
                ans += 1
        connected = uf.groupCount()
        removable = ans + 2 - 2 * connected
        if max(uf1.groupCount(), uf2.groupCount()) > 1 or removable < 0:
            return -1
        if connected == 1:
            return ans
        else:
            return removable
