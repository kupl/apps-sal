class UF:

    def __init__(self, n):
        self.p = [i for i in range(n)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        (px, py) = (self.find(x), self.find(y))
        if px == py:
            return False
        self.p[py] = px
        return True


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        (A, B) = (set(), set())
        (rmA, rmB) = (0, 0)
        for (t, u, v) in edges:
            if t == 1:
                if (-3, u, v) in A:
                    rmA += 1
                else:
                    A.add((-1, u, v))
            elif t == 2:
                if (-3, u, v) in B:
                    rmB += 1
                else:
                    B.add((-2, u, v))
            else:
                if (-1, u, v) in A:
                    rmA += 1
                    A.remove((-1, u, v))
                if (-2, u, v) in B:
                    rmB += 1
                    B.remove((-2, u, v))
                A.add((-3, u, v))
                B.add((-3, u, v))
        common = set()
        ufa = UF(n + 1)
        ufb = UF(n + 1)
        eA = eB = 0
        for (t, u, v) in sorted(A):
            if ufa.union(u, v):
                eA += 1
            elif t == -1:
                rmA += 1
            else:
                common.add((u, v))
        for (t, u, v) in sorted(B):
            if ufb.union(u, v):
                eB += 1
            elif t == -2:
                rmB += 1
            else:
                common.add((u, v))
        return rmA + rmB + len(common) if eA == eB == n - 1 else -1
