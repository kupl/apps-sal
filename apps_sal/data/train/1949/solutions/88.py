class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        def helper(i, j, a):
            if i in [-1, len(grid)] or j in [-1, len(grid[0])] or grid[i][j] in [-1, 0]:
                return a
            y = grid[i][j]; x = a + y; 
            grid[i][j] = -1
            a = max(helper(i+1, j, x), helper(i-1, j, x), helper(i, j+1, x), helper(i, j-1, x))
            grid[i][j] = y
            return a
            
        ans = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = max(ans, helper(i, j, 0))
              
        return ans

