class Solution:

    def numSpecial(self, mat: List[List[int]]) -> int:
        mat_t = list(zip(*mat))
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat_t)):
                if mat[i][j] == sum(mat[i]) == sum(mat_t[j]) == 1:
                    res += 1
        return res
