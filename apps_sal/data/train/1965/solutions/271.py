class UnionFindSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n
        self.count = 1

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        elif self.ranks[pv] > self.ranks[pu]:
            self.parents[pu] = pv
        else:
            self.parents[pu] = pv
            self.ranks[pv] += 1
        self.count += 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf1, uf2 = UnionFindSet(n), UnionFindSet(n)
        ans = 0
        for t, u, v in edges:
            u -= 1
            v -= 1
            if t != 3:
                continue
            flag = 0
            if not uf1.union(u, v):
                flag = 1
            if not uf2.union(u, v):
                flag = 1
            ans += flag

        for t, u, v in edges:
            u -= 1
            v -= 1
            if t == 1:
                if not uf1.union(u, v):
                    ans += 1
            elif t == 2:
                if not uf2.union(u, v):
                    ans += 1
        if uf1.count != n or uf2.count != n:
            return -1
        return ans
