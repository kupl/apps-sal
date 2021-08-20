class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:

        def DFS(row, col):
            if row < 0 or row >= nrow or col < 0 or (col >= ncol):
                return True
            elif grid[row][col] == 1:
                return False
            else:
                grid[row][col] = 1
                connect_boundary = False
                for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    (new_row, new_col) = (row + dx, col + dy)
                    if DFS(new_row, new_col):
                        connect_boundary = True
                return connect_boundary
        (nrow, ncol) = (len(grid), len(grid[0]))
        cnt = 0
        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == 0:
                    if not DFS(row, col):
                        cnt += 1
        return cnt
