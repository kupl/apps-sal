class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        l = len(grid)
        w = len(grid[0])
        seen = set()
        r = 0

        for x in grid:
            print(x)

        def dfs(x, y, gold):
            if (x, y) not in seen and 0 <= x < l and 0 <= y < w and grid[x][y]:
                seen.add((x, y))
                gold += grid[x][y]
                dfs(x + 1, y, gold)
                dfs(x, y + 1, gold)
                dfs(x - 1, y, gold)
                dfs(x, y - 1, gold)
                seen.remove((x, y))
            else:
                nonlocal r
                r = max(r, gold)

        for i in range(l):
            for j in range(w):
                dfs(i, j, 0)

        return r
