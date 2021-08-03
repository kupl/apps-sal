class Solution:
    #
    # Solution 1: DP
    #
    def countSquares1(self, grid: List[List[int]]) -> int:
        n = len(grid); m = len(grid[0]) if grid else 0
        
        res = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0: continue
                if r==0 or c==0: res += 1; continue
                grid[r][c] = min(grid[r-1][c-1], grid[r][c-1], grid[r-1][c]) + 1
                res += grid[r][c]
        return res
    
    #
    # Solution 2: Brute Force
    #
    def countSquares(self, grid):
        n = len(grid); m = len(grid[0]) if grid else 0
        
        def helper(sr, sc, k):
            res = 1
            for i in range(2, k+1):
                j = i-1; er = sr+j; c = sc+j
                for r in range(sr, er+1):
                    if   r == er and any(grid[r][c] == 0 for c in range(sc, sc+i)): return res
                    elif r != er and     grid[r][c] == 0: return res
                res += 1
            return res
        
        res = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0: continue
                res += helper(r, c, min(n-r, m-c))
        return res
    
\"\"\"
[[0,1,1,1],[1,1,1,1],[0,1,1,1]]
[[0,1,1,1],[1,1,0,1],[1,1,1,1],[1,0,1,0]]
\"\"\"    
