class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def backtrack(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            tmp = grid[r][c]
            grid[r][c] = 0
            val = tmp
            val += max(backtrack(r + 1, c), backtrack(r - 1, c), backtrack(r, c + 1), backtrack(r, c - 1))
            grid[r][c] = tmp
            return val

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    tmp = backtrack(i, j)
                    ans = max(ans, tmp)
        return ans
