class Solution:

    def minFallingPathSum(self, A: List[List[int]]) -> int:
        g = [[inf] * len(a) for a in A]

        def get(i, j):
            m = inf
            for k in range(0, len(A[0])):
                if k != j:
                    m = min(m, g[i - 1][k])
            return m
        for i in range(len(g)):
            for j in range(len(g[0])):
                if i == 0:
                    g[i][j] = A[i][j]
                else:
                    g[i][j] = min(g[i][j], get(i, j) + A[i][j])
        return min(g[-1])
