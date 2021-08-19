class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:  # this could be a top-left
                    right_edge = n
                    for res_i in range(i, m):
                        if mat[res_i][j] == 0:
                            break
                        for res_j in range(j, right_edge):
                            if mat[res_i][res_j] == 1:
                                res += 1
                            else:
                                right_edge = min(right_edge, res_j)
                                break
        return res
