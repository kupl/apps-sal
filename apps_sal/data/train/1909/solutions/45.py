class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        
        down =  [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        up = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0:
                    down[i][j] = grid[i][j]
                else:
                    if grid[i][j] == 0:
                        continue
                    down[i][j] = down[i-1][j] + grid[i][j]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j == 0:
                    up[i][j] = grid[i][j]
                else:
                    if grid[i][j] == 0:
                        continue
                    up[i][j] = up[i][j-1] + grid[i][j]
        
        ans = 0
        mx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                toSubtract = min(down[i][j], up[i][j])
                while(toSubtract > mx):
                    nj = j - toSubtract + 1
                    ni = i - toSubtract + 1
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and down[i][nj] >= toSubtract and up[ni][j] >= toSubtract:
                        ans = max(ans, toSubtract)
                    toSubtract -= 1
        
        return ans*ans
