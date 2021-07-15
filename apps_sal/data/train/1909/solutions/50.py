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
                tmp = 0
                s = min(len(grid)-i, len(grid[0])-j)
                while tmp < s:
                    if horizon[i][j+s-1] >= s and horizon[i+s-1][j+s-1] >= s and vertical[i+s-1][j] >= s and vertical[i+s-1][j+s-1] >= s:
                        tmp = s
                    s -= 1
                res = max(res, tmp)
                
        return res*res
                

