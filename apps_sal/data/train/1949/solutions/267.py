class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m=len(grid)
        n=len(grid[0])
        
        def get(i,j):
            
            
            
            if i>=0 and i<m and j>=0 and j<n and grid[i][j]!=0:
                gold=grid[i][j]
                grid[i][j]=0
                
                maxx=gold+max(get(i+1,j),get(i-1,j), get(i,j+1),get(i,j-1))
                grid[i][j]=gold
            else:
                maxx=0
            return maxx
        maxgold=0
        for i in range(m):
            for j in range(n):
                maxgold=max(maxgold,get(i,j))
        return maxgold

