class Solution:

    def getMaximumGold(self, A: List[List[int]]) -> int:

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return (0, set())
            val = A[i][j]
            if val == 0:
                return (0, set())
            A[i][j] = 0
            maxgold = 0
            maxpath = set()
            for (ni, nj) in ((i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)):
                (gold, path) = dfs(ni, nj)
                if gold > maxgold:
                    maxgold = gold
                    maxpath = path
            A[i][j] = val
            maxpath.add((i, j))
            return (val + maxgold, maxpath)
        maxgold = 0
        maxpath = set()
        (m, n) = (len(A), len(A[0]))
        for i in range(m):
            for j in range(n):
                if (i, j) in maxpath:
                    continue
                (gold, path) = dfs(i, j)
                if gold > maxgold:
                    maxgold = gold
                    maxpath = path
        return maxgold
