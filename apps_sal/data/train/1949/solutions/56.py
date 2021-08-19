class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def visit(i, j):
            visited[i][j] = True
            gold = 0
            if i > 0 and (not visited[i - 1][j]):
                gold = max(gold, visit(i - 1, j))
            if i < m - 1 and (not visited[i + 1][j]):
                gold = max(gold, visit(i + 1, j))
            if j > 0 and (not visited[i][j - 1]):
                gold = max(gold, visit(i, j - 1))
            if j < n - 1 and (not visited[i][j + 1]):
                gold = max(gold, visit(i, j + 1))
            visited[i][j] = False
            return gold + grid[i][j]
        visited = [[False] * n for i in range(m)]

        def reset():
            for i in range(m):
                for j in range(n):
                    visited[i][j] = grid[i][j] == 0
        max_gold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    reset()
                    max_gold = max(max_gold, visit(i, j))
        return max_gold
