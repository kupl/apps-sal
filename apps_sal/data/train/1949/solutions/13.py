class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxCount = 0
        
        N = len(grid)
        M = len(list(zip(*grid)))
        
        for row in range(N):
            for col in range(M):
                if grid[row][col] != 0:
                    maxCount = max(self.backtrack(grid, row, col, N, M), maxCount)
        
        return maxCount
    
    
    def backtrack(self, grid, row, col, N, M):
        value = grid[row][col]
        grid[row][col] = -1
        
        maxCollected = 0
        
        
        if row + 1 < N and grid[row + 1][col] not in (0, -1):
            maxCollected = max(self.backtrack(grid, row + 1, col, N, M), maxCollected)
            
        if col + 1 < M and grid[row][col + 1] not in (0, -1):
            maxCollected = max(self.backtrack(grid, row, col + 1, N, M), maxCollected)
            
        if row - 1 >= 0 and grid[row - 1][col] not in (0, -1):
            maxCollected = max(self.backtrack(grid, row - 1, col, N, M), maxCollected)
            
        if col - 1 >= 0 and grid[row][col - 1] not in (0, -1):
            maxCollected = max(self.backtrack(grid, row, col - 1, N, M), maxCollected)
        
        grid[row][col] = value
        
        return value + maxCollected
