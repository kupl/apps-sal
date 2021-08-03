class UFset:

    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n
        self.size = 1

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.ranks[x] < self.ranks[y]:
            px, py = py, px
        self.parents[px] = py
        self.ranks[py] += 1
        self.size += 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UFset(n)
        bob = UFset(n)
        res = 0
        for type_i, v, w in edges:
            v -= 1
            w -= 1
            if type_i == 3:
                a = alice.union(v, w)
                b = bob.union(v, w)
                if not a and not b:
                    res += 1
        for type_i, v, w in edges:
            v -= 1
            w -= 1
            if type_i == 1:
                if not alice.union(v, w):
                    res += 1
            elif type_i == 2:
                if not bob.union(v, w):
                    res += 1

        return res if alice.size == bob.size == n else -1
