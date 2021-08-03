class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # My original solution, not very fast
        # mat_t = list(zip(*mat))
        # row_s = [i for i in range(len(mat)) if sum(mat[i]) == 1]
        # col_s = [j for j in range(len(mat_t)) if sum(mat_t[j]) == 1]
        # return sum(mat[i][j] == 1 and i in row_s and j in col_s for i in range(len(mat)) for j in range(len(mat_t)))

        # Modified version, still not very fast
        mat_t = list(zip(*mat))
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat_t)):
                if mat[i][j] == sum(mat[i]) == sum(mat_t[j]) == 1:
                    res += 1
        return res
