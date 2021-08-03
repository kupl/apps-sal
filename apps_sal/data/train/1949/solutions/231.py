class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        self.visited = [[False] * C for _ in range(R)]

        def helper(grid, r, c, R, C):
            if r < 0 or c < 0 or r >= R or c >= C or self.visited[r][c] or grid[r][c] == 0:
                return 0
            self.visited[r][c] = True
            max_ = max(helper(grid, r - 1, c, R, C), helper(grid, r + 1, c, R, C), helper(grid, r, c - 1, R, C), helper(grid, r, c + 1, R, C))
            self.visited[r][c] = False
            return max_ + grid[r][c]

        ans = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] != 0:
                    ans = max(ans, helper(grid, r, c, R, C))

        return ans
