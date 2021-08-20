class Solution:

    @staticmethod
    def get_neis(x, y):
        return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        k = min(k, m + n)
        grid_mem = [[[math.inf] * n for _ in range(m)] for ki in range(k + 1)]
        grid_mem[0][0][0] = 0
        visited = {(0, 0)}
        q = collections.deque([(0, 0)])
        while len(q) > 0:
            (i, j) = q.popleft()
            for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and ((x, y) not in visited) and (grid[x][y] == 0):
                    grid_mem[0][x][y] = grid_mem[0][i][j] + 1
                    visited.add((x, y))
                    q.append((x, y))
        for ki in range(1, k + 1):
            grid_mem[ki][0][0] = 0
            visited = {(0, 0)}
            q = collections.deque([(0, 0)])
            while len(q) > 0:
                (i, j) = q.popleft()
                for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < m and 0 <= y < n and ((x, y) not in visited):
                        level = ki if grid[x][y] == 0 else ki - 1
                        path = math.inf
                        for (x2, y2) in self.get_neis(x, y):
                            if 0 <= x2 < m and 0 <= y2 < n:
                                path = min(path, grid_mem[level][x2][y2])
                        grid_mem[ki][x][y] = path + 1
                        visited.add((x, y))
                        q.append((x, y))
        if grid_mem[-1][-1][-1] < math.inf:
            return grid_mem[-1][-1][-1]
        else:
            return -1
