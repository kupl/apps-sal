class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        iMax = len(grid)
        jMax = len(grid[0])
        
        table = [[[0, 0] for j in range(jMax+1)] for i in range(iMax+1)]
        
        ans = 0
        
        for i in range(1, iMax+1):
            for j in range(1, jMax+1):
                if grid[i-1][j-1] == 1:
                    table[i][j][0] = table[i-1][j][0]+ 1
                    table[i][j][1] = table[i][j-1][1] + 1
                for k in range(min(table[i][j]), 0, -1):
                    if min(table[i-k+1][j][1], table[i][j-k+1][0]) >= k:
                        ans = max(ans, k)
                        break
        return ans*ans
