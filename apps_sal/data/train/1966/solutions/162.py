
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        res = 0
        m = mat

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if j > 0 and mat[i][j] == 1:
                    m[i][j] = m[i][j - 1] + 1

        for j in range(len(mat[0])):
            for i in range(len(mat)):
                mn = m[i][j]

                for k in range(i, -1, -1):
                    mn = min(mn, m[k][j])
                    if mn == 0:
                        break
                    res += mn
        return res
