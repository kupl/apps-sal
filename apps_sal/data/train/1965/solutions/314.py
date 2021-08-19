class Solution:

    def find(self, v):
        if self.vertices[v] != v:
            self.vertices[v] = self.find(self.vertices[v])
        return self.vertices[v]

    def union(self, u, v):
        (up, vp) = (self.find(u), self.find(v))
        if up == vp:
            return False
        self.vertices[up] = vp
        return True

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        self.vertices = list(range(n + 1))
        (e1, e2, ret) = (0, 0, 0)
        for (t, u, v) in edges:
            if t != 3:
                continue
            if self.union(u, v):
                e1 += 1
                e2 += 1
            else:
                ret += 1
        self.vertices_sved = self.vertices[:]
        for (t, u, v) in edges:
            if t != 1:
                continue
            if self.union(u, v):
                e1 += 1
            else:
                ret += 1
        if e1 != n - 1:
            return -1
        self.vertices = self.vertices_sved
        for (t, u, v) in edges:
            if t != 2:
                continue
            if self.union(u, v):
                e2 += 1
            else:
                ret += 1
        if e2 != n - 1:
            return -1
        return ret
