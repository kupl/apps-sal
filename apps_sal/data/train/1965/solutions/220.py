class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        self.parent = [i for i in range(n + 1)]
        res = e1 = e2 = 0
        for t, i, j in edges:
            if t == 3:
                if self.union(i, j):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
        self.parent0 = self.parent[:]
        for t, i, j in edges:
            if t == 1:
                if self.union(i, j):
                    e1 += 1
                else:
                    res += 1
        self.parent = self.parent0
        for t, i, j in edges:
            if t == 2:
                if self.union(i, j):
                    e2 += 1
                else:
                    res += 1
        return res if e1 == e2 == n - 1 else -1

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return 0
        self.parent[x] = y
        return 1
