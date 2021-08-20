class DSU:

    def __init__(self, n: int):
        self.p = list(range(n))
        self.e = 0

    def find(self, x: int) -> int:
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def merge(self, x: int, y: int) -> int:
        (rx, ry) = (self.find(x), self.find(y))
        if rx == ry:
            return 1
        self.p[rx] = ry
        self.e += 1
        return 0


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        (A, B) = (DSU(n + 1), DSU(n + 1))
        ans = 0
        for (t, x, y) in edges:
            if t != 3:
                continue
            ans += A.merge(x, y)
            B.merge(x, y)
        for (t, x, y) in edges:
            if t == 3:
                continue
            d = A if t == 1 else B
            ans += d.merge(x, y)
        return ans if A.e == B.e == n - 1 else -1
