class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        count = 0
        r = len(mat)
        c = len(mat[0])
        for i in range(r):
            for j in range(c - 2, -1, -1):
                if mat[i][j] == 1:
                    mat[i][j] += mat[i][j + 1]
        for i in range(r):
            for j in range(c):
                minm = mat[i][j]
                d = i
                while d < r and mat[d][j] != 0:
                    minm = min(minm, mat[d][j])
                    count += minm
                    d += 1
        return count
