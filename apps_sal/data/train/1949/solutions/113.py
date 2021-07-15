class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        
        max_len = 0
        def dfs(trajectory, r, c):
            nonlocal max_len
            count_neighbor = 0
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < nrow and 0 <= nc < ncol and grid[nr][nc] != 0 and (nr, nc) not in trajectory:
                    count_neighbor += 1
                    trajectory.add((nr, nc))
                    dfs(trajectory, nr, nc)
                    trajectory.remove((nr, nc))

            if count_neighbor == 0:
                max_len = max(max_len, sum(grid[i][j] for i, j in trajectory))

        max_len = 0
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] != 0:
                    dfs(set([(r, c)]), r, c)

        return max_len

