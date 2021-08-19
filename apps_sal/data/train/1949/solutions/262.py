class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if not rows:
            return 0
        cols = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 0
            val = grid[i][j]
            grid[i][j] = 0
            _sum = val + max(dfs(i - 1, j), dfs(i, j - 1), dfs(i + 1, j), dfs(i, j + 1))
            grid[i][j] = val
            return _sum

        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i, j))
        return ans

#         m = len(grid)
#         n = len(grid[0])
#         visited = {}

#         def backtrack(path, i, j, start):

#             if grid[i][j] == 0:
#                 # print(path)
#                 return sum(path)

#             for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
#                 if (i + x, j + y) not in visited:
#                     if not (i + x < 0 or j + y < 0 or i + x >= m or j + y >= n):
#                         visited[(i + x, j + y)] = backtrack(path + [grid[i + x][j + y]], i + x, j + y, (i + x, j +y))
#                     else:
#                         visited[(i + x, j + y)] = float('-inf')

#             visited[(i,j)] = sum(path) + max(visited[(i + x, j + y)] for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)))


#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] != 0:
#                     backtrack([grid[i][j]], i, j, (i,j))

#         return
