class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        values = [[0 for j in range(0, m)] for i in range(0, n)]
        visited = [[0 for j in range(0, m)] for i in range(0, n)]
        _max = 0
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] != 0:
                    self._clear(visited)
                    values[i][j] = self._dfs(i, j, grid, visited)
                    _max = max(_max, values[i][j])

        return _max

    def _clear(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        for i in range(0, n):
            for j in range(0, m):
                grid[i][j] = 0

    def _dfs(self, i: int, j: int, grid: List[List[int]], visited: List[List[int]]) -> int:
        if grid[i][j] == 0:
            return 0
        if visited[i][j] != 0:
            return 0

        n = len(grid)
        m = len(grid[0])

        visited[i][j] = 1

        idx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        _max = 0
        for p in idx:
            if i + p[0] >= 0 and i + p[0] < n and j + p[1] >= 0 and j + p[1] < m:
                v = self._dfs(i + p[0], j + p[1], grid, visited)
                _max = max(_max, v)

        visited[i][j] = 0
        return grid[i][j] + _max
