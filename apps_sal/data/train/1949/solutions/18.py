class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j,seen):
            if i < 0 or j < 0 or j >= len(grid[0]) or i >= len(grid) or (i,j) in seen or grid[i][j] == 0:
                return 0
            
            seen.add((i,j))
            
            t = grid[i][j] + max(dfs(i+1,j,seen),
                                    dfs(i,j+1,seen),
                                    dfs(i-1,j,seen),
                                    dfs(i,j-1,seen))
            seen.remove((i,j))
            return t
        
        ans = 0                                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
        
                ans = max(dfs(i,j,set()),ans)
        
        return ans

