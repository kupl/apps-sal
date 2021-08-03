class Solution:
    def __init__(self):
        self.next_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if grid[row][col] == 0:
                return 0

            gold = grid[row][col]
            grid[row][col] = 0

            max_child = 0
            for move in self.next_moves:
                next_row, next_col = row + move[0], col + move[1]
                if -1 < next_row < n and -1 < next_col < m:
                    max_child = max(max_child, dfs(next_row, next_col))

            grid[row][col] = gold
            return gold + max_child

        n = len(grid)
        m = len(grid[0])

        max_gold = 0
        for i in range(n):
            for j in range(m):
                max_gold = max(max_gold, dfs(i, j))
        return max_gold
