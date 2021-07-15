class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        grid_visited = [[0 for i in range(n)] for i in range(m)]
        max_gold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    temp = self.start_mine(grid, grid_visited, i, j)
                    max_gold = max(max_gold, temp)
        return max_gold
                
        
    def start_mine(self, grid, grid_visited, i, j):
        total = grid[i][j]
        max_choice = 0
        grid_visited[i][j] = 1
        #up
        if i-1 >= 0 and grid[i-1][j] != 0 and grid_visited[i-1][j] == 0:
            temp = self.start_mine(grid, grid_visited, i-1, j)
            max_choice = max(temp, max_choice)
        
        #down
        if i+1 < len(grid) and grid[i+1][j] != 0 and grid_visited[i+1][j] == 0:
            temp = self.start_mine(grid, grid_visited, i+1, j)
            max_choice = max(temp, max_choice)
        
        #left
        if j-1 >= 0 and grid[i][j-1] != 0 and grid_visited[i][j-1] == 0:
            temp = self.start_mine(grid, grid_visited, i, j-1)
            max_choice = max(temp, max_choice)
        
        #right
        if j+1 < len(grid[0]) and grid[i][j+1] != 0 and grid_visited[i][j+1] == 0:
            temp = self.start_mine(grid, grid_visited, i, j+1)
            max_choice = max(temp, max_choice)
            
        grid_visited[i][j] = 0
        return total + max_choice
