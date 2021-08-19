class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        (R, C) = (len(grid), len(grid[0]))
        self.visited = [[False] * C for _ in range(R)]
        ans = 0

        def dfs(grid, r, c, R, C):
            if r < 0 or c < 0 or r >= R or (c >= C) or self.visited[r][c] or (grid[r][c] == 0):
                return 0
            self.visited[r][c] = True
            max_ = max(dfs(grid, r - 1, c, R, C), dfs(grid, r + 1, c, R, C), dfs(grid, r, c - 1, R, C), dfs(grid, r, c + 1, R, C)) + grid[r][c]
            self.visited[r][c] = False
            return max_
        for r in range(R):
            for c in range(C):
                ans = max(ans, dfs(grid, r, c, R, C))
        return ans
