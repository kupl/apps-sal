class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        nr = len(grid)
        nc = len(grid[0])

        all_cells = 0
        start = (0, 0)
        res = 0

        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] >= 0:
                    all_cells += 1
                if grid[r][c] == 1:
                    start = (r, c)

        def dfs(r, c, cell_nums):
            nonlocal res
            nonlocal direction
            nonlocal grid
            nonlocal nr
            nonlocal nc

            if grid[r][c] == 2 and cell_nums == 1:
                # reach the destination
                res += 1
                return

            temp = grid[r][c]
            grid[r][c] = -2
            cell_nums -= 1

            for d in direction:
                rr = r + d[0]
                cc = c + d[1]
                if 0 <= rr < nr and 0 <= cc < nc and grid[rr][cc] >= 0:
                    dfs(rr, cc, cell_nums)

            grid[r][c] = temp
        dfs(*start, all_cells)
        return res
