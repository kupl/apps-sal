class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if j != 0 and mat[i][j] == 1:
                    mat[i][j] = mat[i][j - 1] + 1

        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):

                ans = mat[i][j]
                for k in range(i, len(mat)):
                    ans = min(ans, mat[k][j])
                    res += ans

        return res
