class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        r = len(mat)
        c = len(mat[0])
        for i in range(r):
            for j in range(c - 2, -1, -1):
                if mat[i][j] != 0:
                    mat[i][j] = mat[i][j + 1] + 1
        count = 0
        for i in range(r):
            for j in range(c):
                width = mat[i][j]
                for k in range(i, r):
                    width = min(width, mat[k][j])
                    count += width
        return count
