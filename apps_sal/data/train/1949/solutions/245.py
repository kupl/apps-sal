class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        def collect(i,j):
            if not (0 <= i < m and 0 <= j < n and grid[i][j]): return 0
            gold = grid[i][j]
            grid[i][j] = 0
            possible = [collect(i+di,j+dj) for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]]
            grid[i][j] = gold
            return max(possible) + gold
        
        return max(collect(i,j) for i in range(m) for j in range(n))
        
                
                
                    

