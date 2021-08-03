class Solution:
    def minimumMoves(self, grid):
        \"\"\"
        :type grid: List[List[int]]
        :rtype: int
        \"\"\"
        n = len(grid)
        if grid[-1][-1] == 1:
            return -1
        dp = [[[float('inf'), float('inf')] for i in range(n)] for j in range(n)]
        dp[0][0][0] = 0
        for j in range(1, n - 1):
            if grid[0][j + 1] == 0:
                dp[0][j][0] = dp[0][j - 1][0] + 1
            else:
                break
        for i in range(n):
            for j in range(n):
                if j < n - 1 and grid[i][j + 1] == 0:
                    dp[i][j][0] = min(dp[i][j][0], dp[i][j - 1][0] + 1)
                    if grid[i][j] == 0:
                        dp[i][j][0] = min(dp[i][j][0],dp[i - 1][j][0] + 1)
                if i < n - 1 and grid[i + 1][j] == 0:
                    dp[i][j][1] = min(dp[i][j][1], dp[i - 1][j][1] + 1)
                    if grid[i][j] == 0:
                        dp[i][j][1] = min(dp[i][j][1], dp[i][j - 1][1] + 1)
                if i < n - 1 and j < n - 1 and grid[i][j + 1] == grid[i + 1][j] == grid[i + 1][j + 1] == 0:
                    dp[i][j][0], dp[i][j][1] = min(dp[i][j][0], dp[i][j][1] + 1), min(dp[i][j][1], dp[i][j][0] + 1)
        return dp[n - 1][n - 2][0] if dp[n - 1][n - 2][0] < float('inf') else -1


# class Solution:
#     def minimumMoves(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         num_steps_horizontal = [[float('inf') for _ in range(n)] for _ in range(n)]
#         num_steps_vertical = [[float('inf') for _ in range(n)] for _ in range(n)]

#         if not (grid[0][0] == grid[0][1] == 0):
#             raise ValueError

#         # initialization
#         num_steps_horizontal[0][0] = 0
#         for col in range(1, n - 1):
#             if grid[0][col] == 0:
#                 num_steps_horizontal[0][col] = 1 + num_steps_horizontal[0][col - 1]
#             else:
#                 break

#         if grid[1][0] == grid[1][1] == 0:
#             num_steps_vertical[0][0] = 1
#             for row in range(1, n):
#                 if grid[row][0] == 0:
#                     num_steps_vertical[row][0] = 1 + num_steps_vertical[row - 1][0]
#                 else:
#                     break

#         # iterate over num_steps_horizontal and num_steps_vertical
#         for row in range(1, n):
#             for col in range(1, n):
#                 if col < n - 1 and grid[row][col] == grid[row][col + 1] == 0:
#                     num_steps_horizontal[row][col] = 1 + min(
#                         num_steps_horizontal[row][col - 1], # from left 
#                         num_steps_horizontal[row - 1][col], # from above
#                         )
#                 if row < n - 1 and grid[row][col] == grid[row + 1][col] == 0:
#                     num_steps_vertical[row][col] = 1 + min(
#                         num_steps_vertical[row][col - 1], # from left 
#                         num_steps_vertical[row - 1][col], # from above
#                         )
#                 if (col < n - 1 and row < n - 1
#                    and grid[row][col] == grid[row][col + 1] == 0
#                    and grid[row][col] == grid[row + 1][col] == 0):
#                     num_steps_horizontal[row][col] = min(num_steps_horizontal[row][col], 1 + num_steps_vertical[row][col])
#                     num_steps_vertical[row][col] = min(num_steps_vertical[row][col], 1 + num_steps_horizontal[row][col])
                    
#         if num_steps_horizontal[-1][-2] < float('inf'):
#             return num_steps_horizontal[-1][-2]
#         else:
#             return -1
