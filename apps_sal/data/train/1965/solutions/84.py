class UnionFind:
    def __init__(self, size):
        self.father = [i for i in range(size + 1)]

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def connect(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b


class Solution:
    def mst(self, n, edges, t):
        g = sorted([e for e in edges if e[0] in (t, 3)], key=lambda x: -x[0])
        UF, u = UnionFind(n), set()
        for t, a, b in g:
            if UF.find(a) != UF.find(b):
                UF.connect(a, b)
                u.add((t, a, b))
        return len({UF.find(i) for i in range(1, n + 1)}) == 1, u

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        traversed1, mst1 = self.mst(n, edges, 1)
        traversed2, mst2 = self.mst(n, edges, 2)
        if (not traversed1) or (not traversed2):
            return -1
        return len(edges) - len(mst1 | mst2)
