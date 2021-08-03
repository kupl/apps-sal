class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j, cur):
            nonlocal mx
            cur += grid[i][j]
            mx = max(mx, cur)
            path.add((i, j))
            for I, J in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= I < len(grid) and 0 <= J < len(grid[0]) and grid[I][J] != 0 and (I, J) not in path:
                    dfs(I, J, cur)
            path.remove((i, j))

        if not grid:
            return 0
        mx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    path = set()
                    dfs(i, j, 0)
        return mx
