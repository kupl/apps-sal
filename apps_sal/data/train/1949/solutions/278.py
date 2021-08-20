class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        nR = len(grid)
        nC = len(grid[0])
        vis = [[0 for i in range(nC)] for j in range(nR)]
        steps = [[0, -1], [-1, 0], [1, 0], [0, 1]]
        _max = 0
        for r in range(nR):
            for c in range(nC):
                cell = grid[r][c]
                if cell == 0:
                    vis[r][c] = -1
        for r in range(nR):
            for c in range(nC):
                if vis[r][c] == -1:
                    continue
                _max = max(_max, self.dfs(grid, vis, r, c, nR, nC, steps))
        return _max

    def dfs(self, grid, vis, r, c, nR, nC, steps):
        vis[r][c] = -1
        cell = grid[r][c]
        _max = cell
        for step in steps:
            _r = r + step[0]
            _c = c + step[1]
            if 0 <= _r < nR and 0 <= _c < nC and (grid[_r][_c] != 0) and (vis[_r][_c] == 0):
                _max = max(_max, cell + self.dfs(grid, vis, _r, _c, nR, nC, steps))
        vis[r][c] = 0
        return _max
