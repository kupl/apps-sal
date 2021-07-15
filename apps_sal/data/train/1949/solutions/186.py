class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        maxi=0
        
        def findMaxGold(r,c):
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] == 0: return 0
            origin = grid[r][c]
            grid[r][c] = 0  # mark as visited
            maxGold = 0
            for nr, nc in ((r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)):
                maxGold = max(findMaxGold(nr, nc), maxGold)
            grid[r][c] = origin  # backtrack
            return maxGold + origin
                
        for i in range(m):
            for j in range(n):
                maxi = max(maxi,findMaxGold(i,j))
                    
        return(maxi)
