class DSU:

    def __init__(self, a):
        self.par = {x: x for x in a}

    def merge(self, u, v):
        rootu = self.find(u)
        rootv = self.find(v)

        if rootu == rootv:
            return False

        self.par[rootv] = rootu
        return True

    def find(self, u):
        if self.par[u] != u:
            self.par[u] = self.find(self.par[u])
        return self.par[u]


class Solution:
    def minCostConnectPoints(self, a: List[List[int]]) -> int:

        def manhattan_dist(u, v):
            return abs(u[0] - v[0]) + abs(u[1] - v[1])

        n = len(a)

        a = [tuple(x) for x in a]

        dsu = DSU(a)

        edges = []

        for u, v in combinations(a, 2):
            edges.append((u, v, manhattan_dist(u, v)))

        edges.sort(key=lambda x: x[2])

        ret = 0

        for u, v, c in edges:
            if dsu.merge(u, v):
                ret += c

        return ret
