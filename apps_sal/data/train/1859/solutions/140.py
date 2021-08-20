class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 1:
            return matrix[0][0]
        count = [[[0] * 3 for i in range(n + 1)] for _ in range(m + 1)]
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1]:
                    count[i][j][0] = count[i - 1][j][0] + 1
                    count[i][j][1] = count[i][j - 1][1] + 1
                    count[i][j][2] = min(count[i - 1][j - 1][2], count[i - 1][j][0], count[i][j - 1][1]) + 1
                    res += count[i][j][2]
        return res
