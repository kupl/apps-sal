class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        row=[[0]*(m+1) for i in range(n+1)]
        col=[[0]*(m+1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                row[i][j]=row[i][j-1]+grid[i-1][j-1]
                col[i][j]=col[i-1][j]+grid[i-1][j-1]
        res=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if grid[i-1][j-1]:
                    k=1
                    res=max(res,1)
                    while i+k<=n and j+k<=m:
                        if row[i][j+k]-row[i][j-1]==row[i+k][j+k]-row[i+k][j-1]==col[i+k][j]-col[i-1][j]==col[i+k][j+k]-col[i-1][j+k]==k+1:
                            res=max(res,(k+1)*(k+1))
                        k+=1
        return res
        
        
        
        

