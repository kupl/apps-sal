import numpy as np
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        ans = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        print(ans)
        mat = np.array(mat)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                a = i - k if i - k >= 0 else 0
                b = i + k if i + k <= len(mat) else len(mat)
                c = j - k if j - k >= 0 else 0
                d = j + k if j + k <= len(mat[0]) else len(mat[0])
                ans[i][j] = np.sum(mat[a : b + 1, c : d + 1])
        return ans
        

