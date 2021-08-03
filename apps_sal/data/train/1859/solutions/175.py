class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0

        @lru_cache(None)
        def search(i, j):
            nonlocal res
            if i >= m or i < 0 or j >= n or j < 0:
                return 0

            val = (1 + min(search(i - 1, j), search(i, j - 1), search(i - 1, j - 1))) * matrix[i][j]
            res += val
            return val

        search(m - 1, n - 1)
        return res
