import copy


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return 0

        self.parent[px] = py
        return 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf, res, e1, e2 = UnionFind(n), 0, 0, 0
        for _, u, v in [x for x in edges if x[0] == 3]:
            add = uf.union(u, v)
            if add:
                e1 += 1
                e2 += 1
            else:
                res += 1

        uf1 = copy.deepcopy(uf)
        for _, u, v in [x for x in edges if x[0] == 1]:
            add = uf1.union(u, v)
            if add:
                e1 += 1
            else:
                res += 1

        uf2 = uf
        for _, u, v in [x for x in edges if x[0] == 2]:
            add = uf2.union(u, v)
            if add:
                e2 += 1
            else:
                res += 1

        return res if e1 == n - 1 and e2 == n - 1 else -1
