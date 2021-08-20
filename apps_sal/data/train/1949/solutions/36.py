class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        (R, C) = (len(grid), len(grid[0]))

        def traverse(r, c):
            if not (0 <= r < R and 0 <= c < C):
                return 0
            if not grid[r][c]:
                return 0
            cur = grid[r][c]
            grid[r][c] = 0
            res = 0
            for (x, y) in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                res = max(res, traverse(r + x, c + y))
            res += cur
            grid[r][c] = cur
            return res
        result = 0
        for r in range(R):
            for c in range(C):
                result = max(result, traverse(r, c))
        return result
