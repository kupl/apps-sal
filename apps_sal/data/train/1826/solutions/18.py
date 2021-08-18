class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:

        mat2 = copy.deepcopy(mat)

        def help(i, j, K):
            res = 0
            for ii in range(i - K, i + K + 1):
                for jj in range(j - K, j + K + 1):
                    if 0 <= ii < len(mat) and 0 <= jj < len(mat[0]):
                        res += mat[ii][jj]
            return res

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if j == 0:
                    mat2[i][j] = help(i, j, K)
                else:
                    mat2[i][j] = mat2[i][j - 1]
                    if j + K < len(mat[0]):
                        for ii in range(i - K, i + K + 1):
                            if 0 <= ii < len(mat):
                                mat2[i][j] += mat[ii][j + K]
                    if j - K - 1 >= 0:
                        for ii in range(i - K, i + K + 1):
                            if 0 <= ii < len(mat):
                                mat2[i][j] -= mat[ii][j - K - 1]

        return mat2
