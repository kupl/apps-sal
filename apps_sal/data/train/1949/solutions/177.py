class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        d=[]
        m=len(grid)
        n=len(grid[0])
        gold=[]
        for i in range(m):
            for j in range(n):
                if grid[i][j]>0:
                    gold.append((i,j))
        d=[[1,0],[-1,0],[0,1],[0,-1]]
        
        def dfs(x,y,seen):
            if (x,y) in seen or x<0 or x>=m or y<0 or y>=n or grid[x][y]<=0:
                return 0
            a=seen.copy()
            a.add((x,y))
            return grid[x][y]+max(dfs(x+dx,y+dy,a) for dx,dy in d)
        
        return max(dfs(x,y,set()) for x,y in gold)

