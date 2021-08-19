class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        import numpy as np
        mat = np.array(mat)
        ans = []
        for i in range(mat.shape[0]):
            temp = []
            for j in range(mat.shape[1]):
                left = 0 if i - K < 0 else i - K
                right = i + K + 1
                up = 0 if j - K < 0 else j - K
                down = j + K + 1
                temp.append(np.sum(mat[left:right, up:down]))
            ans.append(temp)
        return ans
