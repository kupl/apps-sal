class UF:
    def __init__(self, n):
        self.count = n
        self.parents = [0] * (n + 1)
        for i in range(1 + n):
            self.parents[i] = i

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x == p_y:
            return False
        self.parents[p_x] = p_y
        self.count -= 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufa = UF(n)
        ufb = UF(n)
        res = 0
        for t, u, v in edges:
            if t == 3:
                flag1 = ufa.union(u, v)
                flag2 = ufb.union(u, v)
                if not flag1 and not flag2:
                    res += 1
        for t, u, v in edges:
            if t == 1:
                if not ufa.union(u, v):
                    res += 1
            if t == 2:
                if not ufb.union(u, v):
                    res += 1
        print((ufa.count, ufb.count))
        if ufa.count != 1 or ufb.count != 1:
            return -1
        return res
