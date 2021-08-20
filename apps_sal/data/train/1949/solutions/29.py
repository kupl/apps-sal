class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        totals = []

        def mine(m, n, g, x):
            if m >= 0 and m < len(x) and (n >= 0) and (n < len(x[m])) and (x[m][n] > 0):
                g += x[m][n]
                backup = x[m][n]
                x[m][n] = 0
                mine(m + 1, n, g, x)
                mine(m - 1, n, g, x)
                mine(m, n + 1, g, x)
                mine(m, n - 1, g, x)
                x[m][n] = backup
            totals.append(g)
        for m in range(0, len(grid)):
            for n in range(0, len(grid[m])):
                mine(m, n, 0, grid)
        return max(totals)
