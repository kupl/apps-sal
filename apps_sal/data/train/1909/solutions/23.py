class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        left_reach = [row[:] for row in grid]
        up_reach = [row[:] for row in grid]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if j > 0:
                        left_reach[i][j] = left_reach[i][j - 1] + 1
                    if i > 0:
                        up_reach[i][j] = up_reach[i - 1][j] + 1
        
        for size in range(min(m, n), 0, -1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    if left_reach[i][j + size - 1] >= size and left_reach[i + size - 1][j + size - 1] >= size \\
                    and up_reach[i + size - 1][j] >= size and up_reach[i + size - 1][j + size - 1] >= size:
                        return size * size
        return 0



#         m, n = len(grid), len(grid[0])
#         left_reach = [[0] * n for _ in range(m)]
#         up_reach = [[0] * n for _ in range(m)]
#         for i in range(m):
#             ones = 0
#             for j, num in enumerate(grid[i]):
#                 if num:
#                     ones += 1
#                 else:
#                     ones = 0
#                 left_reach[i][j] = ones
#             ones = 0
        
#         for j in range(n):
#             ones = 0
#             for i in range(m):
#                 if grid[i][j]:
#                     ones += 1
#                 else:
#                     ones = 0
#                 up_reach[i][j] = ones
                
#         for size in range(min(m, n), 0, -1):
#             for i in range(m - size + 1):
#                 for j in range(n - size + 1):
#                     if left_reach[i][j + size - 1] >= size and left_reach[i + size - 1][j + size - 1] >= size \\
#                     and up_reach[i + size - 1][j] >= size and up_reach[i + size - 1][j + size - 1] >= size:
#                         return size * size
#         return 0
        
        
        
#         m, n = len(grid), len(grid[0])
#         left_reach = [[0] * n for _ in range(m)]
#         right_reach = [[0] * n for _ in range(m)]
#         up_reach = [[0] * n for _ in range(m)]
#         down_reach = [[0] * n for _ in range(m)]
#         for i in range(m):
#             ones = 0
#             for j, num in enumerate(grid[i]):
#                 if num:
#                     ones += 1
#                 else:
#                     ones = 0
#                 left_reach[i][j] = ones
#             ones = 0
#             for j in range(n - 1, -1, -1):
#                 if grid[i][j]:
#                     ones += 1
#                 else:
#                     ones = 0
#                 right_reach[i][j] = ones
        
#         for j in range(n):
#             ones = 0
#             for i in range(m):
#                 if grid[i][j]:
#                     ones += 1
#                 else:
#                     ones = 0
#                 up_reach[i][j] = ones
#             ones = 0
#             for i in range(m - 1, -1, -1):
#                 if grid[i][j]:
#                     ones += 1
#                 else:
#                     ones = 0
#                 down_reach[i][j] = ones
                
#         for size in range(min(m, n), 0, -1):
#             for i in range(m - size + 1):
#                 for j in range(n - size + 1):
#                     if right_reach[i][j] >= size and down_reach[i][j] >= size and left_reach[i + size - 1][j + size - 1] >= size and up_reach[i + size - 1][j + size - 1] >= size:
#                         return size * size
#         return 0
                       
