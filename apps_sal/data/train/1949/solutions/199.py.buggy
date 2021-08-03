class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        def helper(r, c, total, visited):
            nonlocal maxx
            if r < 0 or r >= rows or c < 0 or c >= cols or\\
                grid[r][c] == 0 or (r, c) in visited:
                return
            total += grid[r][c]
            maxx = max(maxx, total)
            helper(r + 1, c, total, visited + [(r, c)])
            helper(r - 1, c, total, visited + [(r, c)])
            helper(r, c + 1, total, visited + [(r, c)])
            helper(r, c - 1, total, visited + [(r, c)])
        
        greatest = 0
        
        starts = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    maxx = 0
                    helper(row, col, 0, [])
                    greatest = max(maxx, greatest)
                    
        return greatest
