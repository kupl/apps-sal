class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        (e0, e1, res) = (0, 0, 0)
        self.root = [i for i in range(n + 1)]

        def find(x):
            if x == self.root[x]:
                return x
            self.root[x] = find(self.root[x])
            return self.root[x]

        def isReachable(x, y):
            (x, y) = (find(x), find(y))
            if x == y:
                return True
            self.root[x] = y
            return False
        for (t, i, j) in edges:
            if t == 3:
                if isReachable(i, j):
                    res += 1
                else:
                    e0 += 1
                    e1 += 1
        root_cpy = self.root[:]
        for (t, i, j) in edges:
            if t == 1:
                if isReachable(i, j):
                    res += 1
                else:
                    e0 += 1
        self.root = root_cpy
        for (t, i, j) in edges:
            if t == 2:
                if isReachable(i, j):
                    res += 1
                else:
                    e1 += 1
        return res if e0 == e1 == n - 1 else -1
