class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def max_gold(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            origin = grid[i][j]
            grid[i][j] = 0
            max_count = 0
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                max_count = max(max_gold(ni, nj), max_count)
            grid[i][j] = origin
            return max_count + origin
        
        mx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                mx = max(mx, max_gold(i, j))
        
        return mx

