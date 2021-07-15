class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:                    
        def dfs(row, col, cur_sum, visited):
            if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]) or visited[row][col]==1 or grid[row][col]==0:
                return
            visited[row][col] = 1
            cur_sum += grid[row][col]
            self.max_path = max(self.max_path, cur_sum)
            dfs(row+1, col, cur_sum, visited)
            dfs(row-1, col, cur_sum, visited)
            dfs(row, col+1, cur_sum, visited)
            dfs(row, col-1, cur_sum, visited)
            visited[row][col] = 0

        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        self.max_path = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0:
                    dfs(row, col, 0, visited)
        return self.max_path
        
        

                
        
        
                        
                        
                    

