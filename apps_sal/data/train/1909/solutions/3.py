class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        dp = [[0] * len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j > 0:
                    print(f'i{i}')
                    print(f'j{j}')
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                if i >= 1 and j >= 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp [i -1][j - 1] + grid[i][j]
            
                
        res = 0
        print(dp)
        length_range = min(len(grid), len(grid[0]))
        for length in range(length_range):
            for x1 in range(len(grid)- length):
                for y1 in range(len(grid[0]) - length):
                    if x1 == 1 and y1 ==0:
                        print(\"denug\")
                    if (self.getLength(grid, dp, x1, y1, x1 + length, y1) == length + 1 and
                       self.getLength(grid, dp, x1, y1, x1, y1 + length) == length + 1 and
                       self.getLength(grid, dp, x1 + length, y1, x1 + length, y1 + length) == length + 1 and
                       self.getLength(grid, dp, x1, y1 + length, x1 + length, y1 + length) == length + 1):
                        res = (length+1)*(length+1)
        return res               
                    
    def getLength(self, grid, dp, x1, y1, x2, y2):
        area_1 = dp[x1 - 1][y2] if x1 - 1 >= 0 else 0
        area_2 = dp[x2][y1 -1] if y1 -1 >= 0 else 0
        area_3 = dp[x1 -1][y1 - 1] if x1 -1 >= 0 and y1 -1 >= 0 else 0
        return dp[x2][y2] - area_1 - area_2 + area_3
