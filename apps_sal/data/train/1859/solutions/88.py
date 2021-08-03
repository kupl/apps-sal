class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        m = len(matrix)
        n = len(matrix[0])

        @functools.lru_cache(None)
        def dp(i, j):

            if matrix[i][j]:
                if 0 < i and 0 < j:
                    return min(dp(i - 1, j - 1), dp(i - 1, j), dp(i, j - 1)) + 1
                return 1
            return 0

        return sum([dp(i, j) for i in range(m) for j in range(n)])
