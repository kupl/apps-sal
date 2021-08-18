class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        res = 0
        summ = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.in_area(grid, i, j):
                    value = self.dfs(grid, i, j, summ, visited)
                    res = max(res, value)
        return res

    def dfs(self, grid, r, c, summ, visited):
        if not self.in_area(grid, r, c):
            return summ
        if not grid[r][c] or (r, c) in visited:
            return summ

        visited.add((r, c))
        summ += grid[r][c]

        res = 0
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in moves:
            r2 = r + dr
            c2 = c + dc
            value = self.dfs(grid, r2, c2, summ, visited)
            res = max(res, value)
        visited.discard((r, c))
        return res

    def in_area(self, grid, r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])
