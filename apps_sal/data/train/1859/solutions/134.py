from typing import List


class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        counts = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        def get_val(r, c, m):
            if 0 <= r < len(m) and 0 <= c < len(m[0]):
                return m[r][c]
            return 0
        total = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 1:
                    l = get_val(r, c - 1, counts)
                    d = get_val(r - 1, c - 1, counts)
                    u = get_val(r - 1, c, counts)
                    counts[r][c] = 1 + min(l, d, u)
                    total += counts[r][c]
        return total
