class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        ans = 0
        
        for row in range(rows):
            for col in range(cols):
                ans = max(ans, self.dfs(grid,row,col))
        
        return ans
        
    def dfs(self, grid, i, j):
        rows, cols = len(grid), len(grid[0])
        # make sure the curr element is a 1
        
        if not grid[i][j]:
            return 0
        
        last = 0
        for offset in (range(min(rows-i,cols-j))):
            # make sure no 0s
            if not grid[i][j+offset] or not grid[i+offset][j]:
                return (last+1)*(last+1)
            
            if self.isValid(grid, [i,j+offset], [i+offset,j]):
                last = offset
            
        return (last+1)*(last+1)
    
    def isValid(self, grid, right, down):
        while True:
            if not grid[right[0]][right[1]] or not grid[down[0]][down[1]]:
                return False
            if right == down:
                return True
            right[0] += 1
            down[1] += 1
            
\"\"\"
[[1,1,1],[1,1,0],[1,1,1],[0,1,1],[1,1,1]]
        1       1       1
        1       1       0
        1       1       1
        0       1       1
        1       1       1
\"\"\"
        
