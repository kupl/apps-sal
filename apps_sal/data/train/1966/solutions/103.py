class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n_row = len(mat)
        if n_row == 0:
            return 0
        n_col = len(mat[0])
        if n_col == 0:
            return 0

        result = 0
        hist = [0] * (n_col + 1)
        for row in range(n_row):
            min_hist_indices = [-1]
            dp = [0] * (n_col + 1)
            for col in range(n_col):
                hist[col] = 0 if mat[row][col] == 0 else hist[col] + 1

                while hist[col] < hist[min_hist_indices[-1]]:
                    min_hist_indices.pop()

                dp[col] = dp[min_hist_indices[-1]] + hist[col] * (col - min_hist_indices[-1])

                min_hist_indices.append(col)

            result += sum(dp)
        return result
