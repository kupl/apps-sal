import numpy as np


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m == 1 and n == 1:
            return mat
        mat = np.array(mat)
        ans = np.array([[0 for _ in range(n)] for _ in range(m)])
        ans[0, 0] += mat[:min(m, K + 1), :min(n, K + 1)].sum()
        for j in range(1, n):
            ans[0, j] = ans[0, j - 1]
            if j + K < n:
                ans[0, j] += mat[:min(K + 1, m), j + K].sum()
            if j - K > 0:
                ans[0, j] -= mat[:min(K + 1, m), j - K - 1].sum()
        for i in range(1, m):
            ans[i, 0] = ans[i - 1, 0]
            if i + K < m:
                ans[i, 0] += mat[i + K, :min(K + 1, n)].sum()
            if i - K > 0:
                ans[i, 0] -= mat[i - K - 1, :min(K + 1, n)].sum()
        for i in range(1, m):
            for j in range(1, n):
                ans[i, j] = ans[i, j - 1]
                if j + K < n:
                    ans[i, j] += mat[max(0, i - K): min(i + K + 1, m), j + K].sum()
                if j - K > 0:
                    ans[i, j] -= mat[max(0, i - K): min(i + K + 1, m), j - K - 1].sum()
        return ans
