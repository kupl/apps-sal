class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dfs(a, b, board, g, seen):
            nonlocal p
            p = max(p, g)
            for (i, j) in ((a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)):
                if 0 <= i < len(board) and 0 <= j < len(board[0]) and (board[i][j] != 0) and ((i, j) not in seen):
                    seen.add((i, j))
                    dfs(i, j, board, g + board[i][j], seen)
                    seen.remove((i, j))
        p = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    dfs(i, j, grid, grid[i][j], {(i, j)})
        return p
