class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxy = [0]

        print (grid)
        def gold(grid,summ,i,j):
    
            if i<=len(grid)-1 and i>-1 and j<=len(grid[0])-1 and j>-1 and grid[i][j]!=0:
        
                temp = grid[i][j]
    
                grid[i][j]=0
                gold(grid,summ+temp,i+1,j)
                gold(grid,summ+temp,i,j+1)
                gold(grid,summ+temp,i-1,j)
                gold(grid,summ+temp,i,j-1)
                grid[i][j]= temp
            else:
                maxy[0]=max(maxy[0],summ)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    gold(grid,0,i,j)
        return (maxy[0])

