class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    if j > 0:
                        mat[i][j] = mat[i][j - 1] + 1
        # for i in range(m):
        #     for j in range(n):
        #         if mat[i][j]:
        #             if i > 0:
        #                 mat[i][j] = mat[i - 1][j] + 1

        total = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    row = i
                    width = mat[i][j]
                    while row < m and mat[row][j]:
                        width = min(width, mat[row][j])
                        total += width
                        row += 1

        return total
