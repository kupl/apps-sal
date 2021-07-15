class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        
        horizon = [[0]*len(grid[0]) for _ in range(len(grid))]
        vertical = [[0]*len(grid[0]) for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    horizon[i][j] = horizon[i][j-1] + 1

        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[j][i] == 1:
                    vertical[j][i] = vertical[j-1][i] + 1
                    
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                s = min(horizon[i][j], vertical[i][j])
                for k in range(s, 0, -1):
                    if horizon[i-k+1][j] >= k and vertical[i][j-k+1] >= k:
                        res = max(res, k)
                        break
                        
                
        return res*res
                

