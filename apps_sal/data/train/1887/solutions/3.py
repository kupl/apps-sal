class Solution:
    def findCircleNum(self, M):
        size = len(M)
        parents = list(range(size))
        res = size
        for i in range(size):
            for j in range(i + 1, size):
                rooti = self.findRoot(parents, i)
                rootj = self.findRoot(parents, j)
                if rooti != rootj and M[i][j] == 1:
                    parents[rootj] = rooti
                    res -= 1
        return res

    def findRoot(self, parents, i):
        return i if parents[i] == i else self.findRoot(parents, parents[i])
