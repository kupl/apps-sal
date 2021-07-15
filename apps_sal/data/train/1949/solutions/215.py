class Solution:
    maxValue=float(\"-inf\")
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        visited=set()
        def dfs(x,y,sum):
            if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]!=0 and (x,y) not in visited :
                visited.add((x,y))
                sum=sum+grid[x][y]
                self.maxValue=max(self.maxValue,sum)
                for p,q in directions:
                    dfs(x+p,y+q,sum)
                    
                visited.remove((x,y))    
        
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]!=0:
                    dfs(i,j,0)
        return self.maxValue
