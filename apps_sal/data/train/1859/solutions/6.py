class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])

        ans = 0
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 1 and i > 0 and j > 0:
                    cand = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1])
                    matrix[i][j] = (cand + 1)
                ans += matrix[i][j]
        return ans
