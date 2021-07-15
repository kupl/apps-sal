class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        for j in range(n):
            for i in range(1, m):
                if mat[i][j]:
                    mat[i][j] += mat[i-1][j]
        print(mat)
        for j in range(n-1, -1, -1):
            for i in range(m):
                if mat[i][j]:
                    minval = mat[i][j]
                    for k in range(j - 1, -1, -1):
                        if mat[i][k] == 0:
                            break
                        minval = min(minval, mat[i][k])
                        mat[i][j] += minval
                res += mat[i][j]
        print(mat)

        return res

