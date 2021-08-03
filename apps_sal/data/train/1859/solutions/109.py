class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        memo = [[0 for x in range(len(matrix[0]) + 1)] for y in range(len(matrix) + 1)]

        for i in range(1, len(memo)):
            for j in range(1, len(memo[0])):

                if matrix[i - 1][j - 1] == 0:
                    memo[i][j] = 0
                else:
                    memo[i][j] = min([memo[i - 1][j - 1], memo[i - 1][j], memo[i][j - 1]]) + 1

        tot = 0
        for i in range(len(memo)):
            for j in range(len(memo[0])):
                tot += memo[i][j]

        return tot
