class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        lefts = [l[:] for l in grid]
        ups = [l[:] for l in grid]
        
        for i in range(n):
            for j in range(1,m):
                if lefts[i][j]:
                    lefts[i][j]+= lefts[i][j-1]

        for j in range(m):
            for i in range(1,n):
                if ups[i][j]:
                    ups[i][j]+= ups[i-1][j]
        
        rec = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    rec = max(rec,1)
                    k = min(ups[i][j], lefts[i][j])
                    for r in range(1,k):
                        if lefts[i-r][j]>=r+1 and ups[i][j-r]>=r+1:
                            rec=max(rec, (r+1)**2)
        
        return rec
