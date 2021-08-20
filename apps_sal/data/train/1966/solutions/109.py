class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        (m, n) = (len(mat), len(mat[0]))
        for i in range(m):
            for j in range(n - 2, -1, -1):
                if mat[i][j] == 1:
                    mat[i][j] += mat[i][j + 1]
        c = 0
        for i in range(m):
            for j in range(n):
                min_ = mat[i][j]
                for d in range(i, m):
                    if not mat[i][j]:
                        continue
                    min_ = min(min_, mat[d][j])
                    c = c + min_
        return c
