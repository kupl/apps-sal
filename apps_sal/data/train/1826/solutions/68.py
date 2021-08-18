class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        res_mat = []
        M = len(mat)
        N = len(mat[0])
        for i, m in enumerate(mat):
            res_list = []
            for j, n in enumerate(m):
                val = 0
                r_min = i - K if i - K > 0 else 0
                r_max = i + K + 1 if i + K + 1 < M else M
                c_min = j - K if j - K > 0 else 0
                c_max = j + K + 1 if j + K + 1 < N else N
                for k in range(r_min, r_max):
                    for l in range(c_min, c_max):
                        val += mat[k][l]
                res_list.append(val)
            res_mat.append(res_list)
        return res_mat
