class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        Inf = float('inf')
        dp = [[(Inf, Inf)] * cols for _ in range(rows)]
        dp[-1][-2] = (0, Inf)
        out = lambda r, c: not (0 <= r < rows and 0 <= c < cols)
        get = lambda r, c: (Inf, Inf) if out(r, c) else dp[r][c]
        canBeHorizontal = lambda r, c: c < cols - 1 and grid[r][c+1] != 1
        canBeVertical = lambda r, c: r < rows - 1 and grid[r+1][c] != 1
        canTransform = lambda r, c: canBeVertical(r, c) and canBeHorizontal(r, c)\\
            and (r < rows - 1 and c < cols - 1 and grid[r+1][c+1] != 1)
        
        HORIZONTAL = 0
        VERTICAL = 1

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if grid[r][c] or (r == rows - 1 and c == cols - 2): continue
                hmove = vmove = Inf
                moveDown = get(r + 1, c)
                moveRight = get(r, c + 1)
                if canBeHorizontal(r, c):
                    hmove = 1 + min(moveDown[HORIZONTAL], moveRight[HORIZONTAL])
                if canBeVertical(r, c):
                    vmove = 1 + min(moveDown[VERTICAL], moveRight[VERTICAL])
                if canTransform(r, c):
                    hmove, vmove = min(hmove, 1 + vmove), min(vmove, 1 + hmove)
                dp[r][c] = (hmove, vmove)
        minSteps = dp[0][0][HORIZONTAL]
        if minSteps == Inf: return -1
        return minSteps
        
