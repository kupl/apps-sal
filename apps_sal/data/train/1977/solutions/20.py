class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        if cols == 0:
            return 0
        count = 0

        def recur(x, y):
            if not 0 <= x < rows or not 0 <= y < cols:
                return False
            if grid[x][y] == 1:
                return True
            grid[x][y] = 1
            right = recur(x + 1, y)
            left = recur(x - 1, y)
            top = recur(x, y + 1)
            bot = recur(x, y - 1)
            return right and left and top and bot
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0 and recur(x, y):
                    count += 1
        return count
