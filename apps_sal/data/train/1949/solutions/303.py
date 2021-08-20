class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]

        def helper(i, j):
            if i < 0 or i >= m or j < 0 or (j >= n) or visited[i][j] or (grid[i][j] == 0):
                return 0
            visited[i][j] = True
            a = helper(i - 1, j)
            b = helper(i, j - 1)
            c = helper(i, j + 1)
            d = helper(i + 1, j)
            visited[i][j] = False
            return grid[i][j] + max(a, max(b, max(c, d)))
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    ans = max(ans, helper(i, j))
        return ans
