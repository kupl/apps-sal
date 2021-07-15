class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        output = 0
        direcs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        def dfs(i, j, gold, seen):
            nonlocal output
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j] == 0:
                output = max(output, gold)
                return
            gold += grid[i][j]
            for di, dj in direcs:
                if (i + di, j + dj) not in seen:
                    seen.add((i + di, j + dj))
                    dfs(i + di, j + dj, gold, seen)
                    seen.remove((i + di, j + dj))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0: dfs(i, j, 0, {(i, j)})
        return output
