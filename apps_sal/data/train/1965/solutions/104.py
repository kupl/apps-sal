class Solution:

    def find(self, x, uf):
        if uf.get(x) == None:
            uf[x] = x
            return x
        if uf[x] != x:
            uf[x] = self.find(uf[x], uf)
        return uf[x]

    def union(self, x, y, uf):
        root1 = self.find(x, uf)
        root2 = self.find(y, uf)
        if root1 == root2:
            return False
        uf[root1] = root2
        return True

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(reverse=True)
        uf1 = {}
        uf2 = {}
        check1 = [False] * n
        check2 = [False] * n
        need = 0
        for (t, n1, n2) in edges:
            if t == 3:
                val1 = self.union(n1, n2, uf1)
                val2 = self.union(n1, n2, uf2)
                if val1 or val2:
                    need += 1
            elif t == 1:
                if self.union(n1, n2, uf1):
                    need += 1
            elif t == 2:
                if self.union(n1, n2, uf2):
                    need += 1
        if len(uf1) != n:
            return -1
        if len(uf2) != n:
            return -1
        uf1_a = [(i, key) for (i, key) in enumerate(uf1)]
        uf2_a = [(i, key) for (i, key) in enumerate(uf2)]
        for (i1, key1) in uf1_a:
            if i1 == 0:
                root1 = self.find(key1, uf1)
            elif self.find(key1, uf1) != root1:
                return -1
        for (i2, key2) in uf2_a:
            if i2 == 0:
                root2 = self.find(key2, uf2)
            elif self.find(key2, uf2) != root2:
                return -1
        return len(edges) - need
