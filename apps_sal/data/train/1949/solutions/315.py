class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        self.ans=0
        m=len(grid)
        n=len(grid[0])
        def backtrack(i,j,sumup):
            nonlocal n,m
            if i<0 or i>m-1 or j<0 or j>n-1 or grid[i][j]==0: return 
            sumup+=grid[i][j]
            self.ans=max(self.ans,sumup)
            temp=grid[i][j]
            grid[i][j]=0
            backtrack(i-1,j,sumup)
            backtrack(i+1,j,sumup)
            backtrack(i,j-1,sumup)
            backtrack(i,j+1,sumup)
            grid[i][j]=temp
        
        for i in range(m):
            for j in range(n):
                backtrack(i,j,0)
        return self.ans
            
            

