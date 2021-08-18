
class DSU:

    def __init__(self, a):
        self.par = {x: x for x in a}

    def merge(self, u, v):
        rootu = self.find(u)
        rootv = self.find(v)
        self.par[rootu] = rootv

    def find(self, u):
        if self.par[u] != u:
            self.par[u] = self.find(self.par[u])
        return self.par[u]


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        dsu1 = DSU(range(1, n + 1))
        dsu2 = DSU(range(1, n + 1))

        both = [edge[1:] for edge in edges if edge[0] == 3]
        alice = [edge[1:] for edge in edges if edge[0] == 1]
        bob = [edge[1:] for edge in edges if edge[0] == 2]

        used = 0

        for u, v in both:
            if dsu1.find(u) != dsu1.find(v):
                dsu1.merge(u, v)
                dsu2.merge(u, v)
                used += 1

        for u, v in alice:
            if dsu1.find(u) != dsu1.find(v):
                dsu1.merge(u, v)
                used += 1

        for u, v in bob:
            if dsu2.find(u) != dsu2.find(v):
                dsu2.merge(u, v)
                used += 1

        if len(set(dsu1.find(u) for u in dsu1.par)) != 1 or len(set(dsu2.find(u) for u in dsu2.par)) != 1:
            return -1

        return len(edges) - used
