class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        for i in range(len(mat)):
            for j in range(1, len(mat[0])):
                if mat[i][j]:
                    mat[i][j] = mat[i][j - 1] + 1
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    row = i
                    width = mat[i][j]
                    while row < len(mat) and mat[row][j]:
                        width = min(width, mat[row][j])
                        row += 1
                        count += width
        return count
