class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        nrows = len(matrix)
        ncols = len(matrix[0])
        dp1 = [0] * ncols
        dp2 = [0] * ncols
        ans = 0
        for row in range(nrows):
            (dp1, dp2) = (dp2, [0] * ncols)
            for col in range(ncols):
                if matrix[row][col] == 0:
                    continue
                if row == 0 or col == 0:
                    dp2[col] = 1
                else:
                    dp2[col] = 1 + min(dp1[col], dp1[col - 1], dp2[col - 1])
                ans += dp2[col]
        return ans
