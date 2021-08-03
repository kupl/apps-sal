class Solution:
    def __init__(self):
        self.max_len = 0

    def isValid(self, r, c, grid):
        if r < 0 or c < 0 or r >= self.M or c >= self.N or grid[r][c] == 0:
            return False
        return True

    def dfs(self, r, c, visited, path_sum, grid):
        if (r, c) in visited or not self.isValid(r, c, grid):
            return
        visited.add((r, c))
        path_sum = path_sum + grid[r][c]
        self.max_len = max(self.max_len, path_sum)
        self.dfs(r + 1, c, set(visited), path_sum, grid)
        self.dfs(r - 1, c, set(visited), path_sum, grid)
        self.dfs(r, c + 1, set(visited), path_sum, grid)
        self.dfs(r, c - 1, set(visited), path_sum, grid)

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.M, self.N = len(grid), len(grid[0])

        for m in range(self.M):
            for n in range(self.N):
                self.dfs(m, n, set(), 0, grid)
        return self.max_len
