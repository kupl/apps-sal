class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def getMaxGold(y, x, gold):
            if y < 0 or y >= m or x < 0 or x >= n or grid[y][x] == 0:
                return gold
            gold += grid[y][x]
            origin, grid[y][x] = grid[y][x], 0
            maxGold = 0
            for ax, ay in action:
                maxGold = max(getMaxGold(y + ay, x + ax, gold), maxGold)
                #maxGold = max(getMaxGold(y+ay,x+ax,gold),maxGold)
            grid[y][x] = origin
            # return maxGold + origin
            return maxGold

        action = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        return max(getMaxGold(y, x, 0) for x in range(n) for y in range(m))
