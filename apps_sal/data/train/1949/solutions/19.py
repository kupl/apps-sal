class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        l=[(1,0),(-1,0),(0,1),(0,-1)]
        vis=set()
        res=[0]
        z=-float('inf')
        def fn(a,b):
            z=-float('inf')
            for c,d in l:
                x,y=a+c,b+d
                if x<0 or x>=m or y<0 or y>=n: continue
                if (x,y) not in vis and grid[x][y]>0:
                    vis.add((x,y))
                    res[0]+=grid[x][y]
                    z=max(z,fn(x,y))
                    res[0]-=grid[x][y]
                    vis.remove((x,y))
            if z==-float('inf'): return res[0]
            return z
        for x in range(m):
            for y in range(n):
                if grid[x][y]>0:
                    vis.add((x,y))
                    res[0]+=grid[x][y]
                    z=max(z,fn(x,y))
                    res[0]-=grid[x][y]
                    vis.remove((x,y))
        if z==-float('inf'): return 0
        return z
