class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = [[0] * (n + 1) for _ in range(m + 1)]
        count = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 1:
                    ans[i][j] = 1 + min(ans[i - 1][j], ans[i - 1][j - 1], ans[i][j - 1])
                    count += ans[i][j]
        return count
