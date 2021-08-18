class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        M = len(mat)
        N = len(mat[0])

        mark = [[0 for _ in range(N)] for _ in range(M)]

        for m in range(M):
            for n in range(N):
                if n == 0:
                    mark[m][n] = mat[m][n]
                else:
                    mark[m][n] = mark[m][n - 1] + 1 if mat[m][n] == 1 else 0
        res = 0
        for bottom in range(M):
            for right in range(N):
                Min = mark[bottom][right]
                for upper in range(bottom + 1)[::-1]:
                    Min = min(Min, mark[upper][right])
                    if Min == 0:
                        break
                    res += Min

        return res
