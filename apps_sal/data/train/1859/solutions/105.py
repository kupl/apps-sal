class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        (m, n) = (len(matrix) if matrix else 0, len(matrix[0]) if matrix else 0)
        table = [[0] * n for _ in range(m)]
        ans = 0
        for (i, j) in product(list(range(m)), list(range(n))):
            if matrix[i][j] and j > 0 and (i > 0):
                table[i][j] = min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1]) + 1
            else:
                table[i][j] = matrix[i][j]
            ans += table[i][j]
        return ans
