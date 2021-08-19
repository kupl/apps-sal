class DisjointSet:
    def __init__(self, n):
        self.parent = {i: i for i in range(1, n + 1)}
        self.rank = {i: 1 for i in range(1, n + 1)}
        self.count = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False  # x, y are already connected
        self.count -= 1
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1

        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ds_a = DisjointSet(n)
        ds_b = DisjointSet(n)

        out = 0
        edges = sorted(edges, key=lambda e: e[0], reverse=True)
        for t, u, v in edges:
            if t == 3:
                if not ds_a.union(u, v):
                    out += 1
                else:
                    ds_b.union(u, v)
            elif t == 2:
                if not ds_b.union(u, v):
                    out += 1
            elif t == 1:
                if not ds_a.union(u, v):
                    out += 1

        if (ds_a.count > 1) or (ds_b.count > 1):
            return -1

        return out
