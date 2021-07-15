class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        visited = set()
        max_gold = 0
        def dfs(r, c, max_gold):
            if (r, c) in visited or grid[r][c] == 0:
                return max_gold
            visited.add((r, c))
            for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if 0 <= r+i < len(grid) and 0 <= c+j < len(grid[0]):
                    max_gold = max(max_gold, grid[r][c] + dfs(r+i, c+j, 0))
            visited.remove((r, c))
            return max_gold
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0:
                    max_gold = max(max_gold, dfs(r, c, 0))
        return max_gold

