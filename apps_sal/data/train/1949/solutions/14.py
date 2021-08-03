class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int, sum: int, seen: set) -> int:
            mx = sum
            for x, y in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)):
                if not (x < 0 or x >= m or y < 0 or y >= n or not grid[x][y] or (x, y) in seen):
                    mx = max(dfs(x, y, sum + grid[x][y], seen | {(x, y)}), mx)

            return mx

        m, n = len(grid), len(grid[0])
        res = 0
        for j in range(n):
            for i in range(m):
                if grid[i][j] != 0:
                    seen = set()
                    seen.add((i, j))
                    sum = grid[i][j]
                    res = max(res, dfs(i, j, sum, seen))
        return res
