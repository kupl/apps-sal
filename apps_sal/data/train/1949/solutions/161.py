class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        def collectGold(r, c, goldSoFar):
            
            pts = [[0,1],[1,0],[-1,0],[0,-1]]
            
            maxGold = goldSoFar
            
            for p in pts:
                nR = p[0] + r
                nC = p[1] + c
                
                if 0 <= nR < len(grid) and 0<= nC < len(grid[0]) and grid[nR][nC] != 0:
                    v = grid[nR][nC]
                    grid[nR][nC] = 0
                    gold = collectGold(nR, nC, goldSoFar + v)
                    maxGold = max(gold, maxGold)
                    grid[nR][nC] = v
                    
            return maxGold
        
        maxGold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    v = grid[i][j]
                    grid[i][j] = 0
                    gold = collectGold(i, j, v)
                    maxGold = max(maxGold, gold)
                    grid[i][j] = v
        return maxGold
                

