import queue


class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:
        output = 0
        m = len(grid)
        n = len(grid[0])
        for ii in range(m):
            for jj in range(n):
                if grid[ii][jj] == 0:
                    q = queue.Queue()
                    q.put((ii, jj))
                    grid[ii][jj] = 2
                    flag = True
                    while not q.empty():
                        (x, y) = q.get()
                        if x == 0 or x == m - 1 or y == 0 or (y == n - 1):
                            flag = False
                        for (dx, dy) in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                            if 0 <= x + dx < m and 0 <= y + dy < n and (grid[x + dx][y + dy] == 0):
                                q.put((x + dx, y + dy))
                                grid[x + dx][y + dy] = 2
                    if flag:
                        output += 1
        return output
