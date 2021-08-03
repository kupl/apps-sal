class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        memo = [[0 for j in range(cols)] for i in range(rows)]
        ans = 0

        if grid[0][0] == 1:
            memo[0][0] = (1, 1)
            ans = 1
        else:
            memo[0][0] = (0, 0)

        for i in range(1, rows):
            if grid[i][0] == 0:
                memo[i][0] = (0, 0)
            else:
                memo[i][0] = (memo[i - 1][0][0] + 1, 1)
                ans = 1

        for j in range(1, cols):
            if grid[0][j] == 0:
                memo[0][j] = (0, 0)
            else:
                memo[0][j] = (1, memo[0][j - 1][1] + 1)
                ans = 1

        for i in range(1, rows):
            for j in range(1, cols):
                if grid[i][j] == 0:
                    memo[i][j] = (0, 0)
                else:
                    memo[i][j] = (memo[i - 1][j][0] + 1, memo[i][j - 1][1] + 1)
                    ans = 1

        for i in range(rows - 1, 0, -1):
            for j in range(cols - 1, 0, -1):
                l_min = min(memo[i][j][0], memo[i][j][1])

                while l_min > ans:
                    if memo[i][j - l_min + 1][0] >= l_min and memo[i - l_min + 1][j][1] >= l_min:
                        ans = l_min
                    l_min -= 1
        return ans * ans
