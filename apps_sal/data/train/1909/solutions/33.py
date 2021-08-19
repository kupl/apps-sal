class Solution:

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        horizon = [row[:] for row in grid]
        for i in range(m):
            for j in range(1, n):
                if horizon[i][j] != 0:
                    horizon[i][j] = horizon[i][j - 1] + 1
        vertical = [row[:] for row in grid]
        for i in range(n):
            for j in range(1, m):
                if vertical[j][i] != 0:
                    vertical[j][i] = vertical[j - 1][i] + 1
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    side = min(horizon[i][j], vertical[i][j])
                    eval = 0
                    for dis in range(side, 0, -1):
                        if horizon[i - dis + 1][j] >= dis and vertical[i][j - dis + 1] >= dis:
                            eval = dis * dis
                            break
                    if eval > result:
                        result = eval
        return result
