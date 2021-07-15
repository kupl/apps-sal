class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        def collect(row, col, visited, curr_sum, ans):
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and visited[row][col] == False and grid[row][col] != 0:
            
                curr_sum += grid[row][col]
                
                ans[0] = max(ans[0], curr_sum)
                
                visited[row][col] = True
                collect(row+1, col, visited, curr_sum, ans)
                collect(row-1, col, visited, curr_sum, ans)
                collect(row, col+1, visited, curr_sum, ans)
                collect(row, col-1, visited, curr_sum, ans)
                visited[row][col] = False
            
            
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        ans = [0]
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0:
                    collect(row, col, visited, 0, ans)
                    
        return ans[0]

