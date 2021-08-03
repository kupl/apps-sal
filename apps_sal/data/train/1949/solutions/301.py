class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        l = len(grid)
        w = len(grid[0])
        seen = set()

        def dfs(x, y):
            if (x, y) not in seen and 0 <= x < l and 0 <= y < w and grid[x][y]:
                seen.add((x, y))
                r = max(dfs(x + 1, y), dfs(x, y + 1), dfs(x - 1, y), dfs(x, y - 1)) + grid[x][y]
                seen.remove((x, y))
                return r
            else:
                return 0

        return max(dfs(i, j) for i in range(l) for j in range(w))
