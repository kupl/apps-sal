class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        ans = 0

        def bfs(x, y):
            queue = [(x, y)]
            near_border = False
            while queue:
                (r, c) = queue.pop(0)
                grid[r][c] = 1
                if r == 0 or c == 0 or r == row - 1 or (c == column - 1):
                    near_border = True
                for (r_, c_) in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    (newr, newc) = (r + r_, c + c_)
                    if 0 <= newr < row and 0 <= newc < column and (grid[newr][newc] == 0):
                        queue.append((newr, newc))
            if not near_border:
                nonlocal ans
                ans += 1
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 0:
                    bfs(r, c)
        return ans
