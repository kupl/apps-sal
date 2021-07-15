class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        csum = msum = 0
        
        def backtrack(r,c):
            direct = [(r-1,c), (r+1,c), (r,c+1), (r,c-1)]
            nonlocal msum, csum
            isbool = True
            for p,q in direct:
                if 0 <= p < m and 0 <= q < n and 0 < grid[p][q]:
                    isbool = False
                    value = grid[p][q]
                    csum += grid[p][q]
                    grid[p][q] = 0
                    backtrack(p,q)
                    grid[p][q] = value
                    csum -= value
            if isbool:
                msum = max(msum, csum)
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    csum = value = grid[i][j] 
                    grid[i][j] = 0
                    
                    backtrack(i,j)
                    
                    grid[i][j] = value
        return msum
