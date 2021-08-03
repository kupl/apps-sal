class Solution:
    def find(self, x, uf):
        if uf[x] != x:
            uf[x] = self.find(uf[x], uf)
        return uf[x]

    def union(self, u, v, uf):
        p1 = self.find(u, uf)
        p2 = self.find(v, uf)
        uf[p1] = p2
        return p1 != p2

    def connected(self, uf):
        parent = set()
        for i in range(len(uf)):
            parent.add(self.find(i, uf))
            if len(parent) > 1:
                return False
        return len(parent) == 1

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges = [[t, u - 1, v - 1] for t, u, v in edges]
        t1_edges = set()
        t2_edges = set()
        t3_edges = set()
        ans = 0

        for t, u, v in edges:
            if t == 1:
                t1_edges.add((u, v))
            elif t == 2:
                t2_edges.add((u, v))
            else:
                if (u, v) in t1_edges:
                    t1_edges.remove((u, v))
                    ans += 1
                if (u, v) in t2_edges:
                    t2_edges.remove((u, v))
                    ans += 1
                t3_edges.add((u, v))

        uf1 = [i for i in range(n)]
        uf2 = [i for i in range(n)]

        for u, v in t3_edges:
            union1 = self.union(u, v, uf1)
            union2 = self.union(u, v, uf2)
            if not union1 and not union2:
                ans += 1

        for u, v in t1_edges:
            if not self.union(u, v, uf1):
                ans += 1
        for u, v in t2_edges:
            if not self.union(u, v, uf2):
                ans += 1

        if not self.connected(uf1) or not self.connected(uf2):
            return -1
        return ans
