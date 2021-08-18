class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    mat[i][j] = mat[i][j - 1] + 1 if j > 0 else 1
                    count += mat[i][j]
                    min_ones = mat[i][j]
                    for k in range(i - 1, -1, -1):
                        min_ones = min(min_ones, mat[k][j])
                        count += min_ones
        return count
