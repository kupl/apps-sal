class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        return solve(n, edges)


class UnionFind():

    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.group = n

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parents[px] = py
            self.group -= 1

    def find(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


def solve(n, edges):
    uf1 = UnionFind(n)
    uf2 = UnionFind(n)
    count = 0
    for t, x, y in edges:
        if t == 3:
            if uf1.find(x) != uf1.find(y):
                uf1.union(x, y)
                uf2.union(x, y)
            else:
                count += 1
    for t, x, y in edges:
        if t == 1:
            if uf1.find(x) != uf1.find(y):
                uf1.union(x, y)
            else:
                count += 1
        if t == 2:
            if uf2.find(x) != uf2.find(y):
                uf2.union(x, y)
            else:
                count += 1

    if uf1.group == 1 and uf2.group == 1:
        return count
    else:
        return -1
