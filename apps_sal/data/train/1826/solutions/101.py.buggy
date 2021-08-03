import numpy as np

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        x_dim = len(mat[0])
        y_dim = len(mat)

        def move_down(mat, y, x_bounds):
            if y >= y_dim or y < 0:
                return 0

            ans = 0
            for x in range(x_bounds[0], x_bounds[1]):
                if -1 < x < x_dim:
                    ans += mat[y][x]
            return ans

        def move_right(mat, y_bounds, x):
            if x >= x_dim or x < 0:
                return 0

            ans = 0
            for y in range(y_bounds[0], y_bounds[1]):
                if -1 < y < y_dim:
                    ans += mat[y][x]
            return ans

        ans = np.array([[0] * len(mat[0])] * len(mat))

        for i in range(0, min(K + 1, y_dim)):
            for j in range(0, min(K + 1, x_dim)):
                ans[0][0] += mat[i][j]

        for i in range(1, y_dim):
            ans[i][0] = ans[i - 1][0] - move_down(mat, i-K-1, (0, K + 1)) + \\
                        move_down(mat, i + K, (0, K + 1))

        for i in range(y_dim):
            for j in range(1, x_dim):
                if (i, j) == (0, 0):
                    continue
                ans[i][j] = ans[i][j - 1] - move_right(mat, (i - K, i + K + 1), j - K - 1) + \\
                            move_right(mat, (i - K, i + K + 1), j + K)
        return ans
        
