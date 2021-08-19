class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        (m, n) = (len(mat), len(mat[0]))
        for i in range(1, m):
            for j in range(n):
                if mat[i][j]:
                    mat[i][j] += mat[i - 1][j]
        result = 0
        for i in range(m):
            for k in range(i, m):
                height = k - i + 1
                width = 0
                for j in range(n):
                    if mat[k][j] >= height:
                        width += 1
                        result += width
                    else:
                        width = 0
        return result
