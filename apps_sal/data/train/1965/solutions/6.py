class DSU:

    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1] * N

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        (par_x, par_y) = (self.find(x), self.find(y))
        if par_x == par_y:
            return False
        if self.size[par_x] < self.size[par_y]:
            (par_x, par_y) = (par_y, par_x)
        self.parent[par_y] = par_x
        self.size[par_x] += self.size[par_y]
        self.size[par_y] = self.size[par_x]
        return True

    def getSize(self, x):
        return self.size[self.find(x)]


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        (alice_graph, bob_graph) = (DSU(n + 1), DSU(n + 1))
        ret = 0
        for (t, start, end) in edges:
            if t == 3:
                if not alice_graph.union(start, end):
                    ret += 1
                bob_graph.union(start, end)
        for (t, start, end) in edges:
            if t == 1:
                if not alice_graph.union(start, end):
                    ret += 1
            if t == 2:
                if not bob_graph.union(start, end):
                    ret += 1
        return ret if alice_graph.getSize(1) == bob_graph.getSize(1) == n else -1
