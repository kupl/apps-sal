class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        class DSU:
            def __init__(self, n):
                self.edge_count = 0
                self.parent = [i for i in range(n + 1)]

            def find(self, x):
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, u, v):
                pu, pv = self.find(u), self.find(v)
                if pu != pv:
                    self.parent[pv] = pu
                    self.edge_count += 1
                    return 0
                return 1

            def get_edge_count(self):
                return self.edge_count

        A, B = DSU(n), DSU(n)

        ans = 0
        for typ, u, v in edges:
            if typ != 3:
                continue
            ans += A.union(u, v)
            B.union(u, v)
        # print(A.get_edge_count(), B.get_edge_count())
        for typ, u, v in edges:
            if typ == 3:
                continue
            if typ == 1:
                ans += A.union(u, v)
            elif typ == 2:
                ans += B.union(u, v)
        # print(A.get_edge_count(), B.get_edge_count())
        if A.get_edge_count() == n - 1 and B.get_edge_count() == n - 1:
            return ans
        else:
            return -1
