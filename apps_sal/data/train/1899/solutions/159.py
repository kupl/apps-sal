class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        nrow = len(grid)
        ncol = len(grid[0])

        q = deque()

        def explore_island(grid, i, j):
            if i < 0 or i >= nrow or j < 0 or j >= ncol or grid[i][j] != 1:
                return
            grid[i][j] = 2
            q.append((i, j, 0))
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                explore_island(grid, ni, nj)

        def get_coordinates(grid):
            for i in range(nrow):
                for j in range(ncol):
                    if grid[i][j] == 1:
                        explore_island(grid, i, j)
                        return
            return
        get_coordinates(grid)

        while q:
            i, j, dist = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if ni >= 0 and ni < nrow and nj >= 0 and nj < ncol and grid[ni][nj] != 2:
                    if grid[ni][nj] == 1:
                        return dist
                    elif grid[ni][nj] == 0:
                        grid[ni][nj] = 2
                        q.append((ni, nj, dist + 1))
