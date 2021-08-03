class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        self.ans = -1

        def helper(i, j):
            if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] == 0 or visited[i][j]:
                return 0

            visited[i][j] = True

            a = helper(i, j + 1)
            b = helper(i, j - 1)
            c = helper(i + 1, j)
            d = helper(i - 1, j)

            total = grid[i][j] + max(max(max(a, b), c), d)
            visited[i][j] = False
            return total

        for i in range(m):
            for j in range(n):
                self.ans = max(self.ans, helper(i, j))

        return self.ans
