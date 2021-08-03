class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rl, cl = len(grid), len(grid[0])
        de = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def solve(x, y, seen):
            temp = 0
            for d in de:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < rl and 0 <= ny < cl and grid[nx][ny] and (nx, ny) not in seen:
                    temp = max(temp, solve(nx, ny, seen | {(x, y)}))
            return temp + grid[x][y]

        ans = 0
        for i in range(rl):
            for j in range(cl):
                if grid[i][j]:
                    ans = max(ans, solve(i, j, set()))
        return ans
