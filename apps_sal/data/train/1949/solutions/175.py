class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        i_len = len(grid)
        j_len = len(grid[0])
        max_shit = 0

        def moves(i, j, amount):
            nonlocal max_shit, i_len, j_len
            if i < 0 or j < 0 or i == i_len or (j == j_len) or (grid[i][j] == 0):
                if amount > max_shit:
                    max_shit = amount
                return
            amount += grid[i][j]
            tmp = grid[i][j]
            grid[i][j] = 0
            moves(i + 1, j, amount)
            moves(i - 1, j, amount)
            moves(i, j + 1, amount)
            moves(i, j - 1, amount)
            grid[i][j] = tmp
        for i in range(i_len):
            for j in range(j_len):
                if grid[i][j] != 0:
                    moves(i, j, 0)
        return max_shit
