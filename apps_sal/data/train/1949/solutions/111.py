class Solution:
    def traverse(self, pos, path_sum, grid, visited):
        self.max_sum = max(self.max_sum, path_sum)
        m = len(grid)
        n = len(grid[0])
        x, y = pos
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            xp = x + dx
            yp = y + dy
            if xp < m and xp >= 0 and yp < n and yp >= 0 and \\
            grid[xp][yp] and (xp, yp) not in visited:
                flag = True
                visited.add((xp, yp))
                self.traverse((xp, yp), path_sum + grid[xp][yp], grid, visited)
        visited.remove((x, y))        
        return
                    
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.max_sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    visited = set()
                    visited.add((i, j))
                    self.traverse((i, j), grid[i][j], grid, visited)
        return self.max_sum
                    
