
class DSU:

    def __init__(self, a):
        self.par = {x: x for x in a}

    def merge(self, u, v):
        rootu = self.find(u)
        rootv = self.find(v)

        if rootu == rootv:
            return False

        self.par[rootu] = rootv
        return True

    def find(self, u):
        if self.par[u] != u:
            self.par[u] = self.find(self.par[u])
        return self.par[u]


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        dsu1 = DSU(range(1, n + 1))
        dsu2 = DSU(range(1, n + 1))

        grouper = defaultdict(list)
        for t, u, v in edges:
            grouper[t].append([u, v])

        both, alice, bob = grouper[3], grouper[1], grouper[2]

        ret = 0

        for u, v in both:
            if not dsu1.merge(u, v):
                ret += 1
            dsu2.merge(u, v)

        for u, v in alice:
            if not dsu1.merge(u, v):
                ret += 1

        for u, v in bob:
            if not dsu2.merge(u, v):
                ret += 1

        if len(set(dsu1.find(u) for u in dsu1.par)) != 1 or len(set(dsu2.find(u) for u in dsu2.par)) != 1:
            return -1

        return ret
