class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        R,C = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        d = collections.defaultdict(int)
        def dfs(grid,row,col,idx):
            grid[row][col] = idx
            total = 1
            for di in directions:
                newrow,newcol = row+di[0], col+di[1]
                if 0<=newrow<R and 0<=newcol<C and grid[newrow][newcol] ==1:
                    total += dfs(grid,newrow,newcol,idx)
            return total
                    
        index = 2
        maxlength = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] ==1:
                    total = 0
                    total = dfs(grid,i,j,index)
                    d[index] = total
                    maxlength = max(maxlength, total)
                    index +=1
        
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] ==0:
                    keyset,length = set(),0
                    for di in directions:
                        newrow,newcol = i+di[0], j+di[1]
                    
                        if 0<=newrow<R and 0<=newcol<C and grid[newrow][newcol] > 1:
                            keyset.add(grid[newrow][newcol])
                    length = sum(d[key] for key in keyset)+1
                    maxlength = max(length,maxlength)
        
        return max(1,maxlength)
        
                            
        
        
                    

