class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        class UnionFind:

            def __init__(self):
                self.parent = {}
                self.e = 0

            def find(self, a):
                if a not in self.parent:
                    self.parent[a] = a
                p = a
                while p != self.parent[p]:
                    p = self.parent[p]
                while a != p:
                    tmp = a
                    self.parent[a] = p
                    a = self.parent[tmp]
                return p

            def union(self, a, b):
                (pa, pb) = (self.find(a), self.find(b))
                if pa != pb:
                    self.parent[pa] = pb
                    self.e += 1
                    return 0
                return 1
        (ufa, ufb) = (UnionFind(), UnionFind())
        ans = 0
        for (t, u, v) in edges:
            if t == 3:
                ans += ufa.union(u, v)
                ufb.union(u, v)
        for (t, u, v) in edges:
            if t == 1:
                ans += ufa.union(u, v)
            if t == 2:
                ans += ufb.union(u, v)
        return ans if ufa.e == n - 1 and ufb.e == n - 1 else -1
