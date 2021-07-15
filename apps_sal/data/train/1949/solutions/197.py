class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def findMaxGold(r: int, c: int) -> int:
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] == 0: return 0
            origin = grid[r][c]
            grid[r][c] = 0  # mark as visited
            maxGold = 0
            for nr, nc in ((r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)):
                maxGold = max(findMaxGold(nr, nc), maxGold)
            grid[r][c] = origin  # backtrack
            return maxGold + origin

        m, n = len(grid), len(grid[0])
        return max(findMaxGold(r, c) for c in range(n) for r in range(m))

