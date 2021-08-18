class UF:
    def __init__(self, n: int):
        self.p, self.e = list(range(n)), 0

    def find(self, x: int):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return 1
        self.p[rx] = ry
        self.e += 1
        return 0


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        A, B = UF(n + 1), UF(n + 1)
        ans = 0
        for t, u, v in edges:
            if t != 3:
                continue
            ans += A.union(u, v)
            B.union(u, v)
        for t, u, v in edges:
            if t == 3:
                continue
            d = A if t == 1 else B
            ans += d.union(u, v)
        return ans if A.e == B.e == n - 1 else -1
