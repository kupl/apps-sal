class Solution:
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        (N, M) = (len(grid), len(grid[0]))
        self.res = 0

        def dfs(x: int, y: int, v: int, done: set):
            self.res = max(self.res, v)
            for (dx, dy) in self.DIRS:
                (xx, yy) = (x + dx, y + dy)
                if not 0 <= xx < N or not 0 <= yy < M or (xx, yy) in done or (grid[xx][yy] == 0):
                    continue
                done.add((xx, yy))
                dfs(xx, yy, v + grid[xx][yy], done)
                done.remove((xx, yy))
        done = set()
        for ii in range(N):
            for jj in range(M):
                zero_num = [idx for (idx, (dx, dy)) in enumerate(self.DIRS) if 0 <= ii + dx < N and 0 <= jj + dy < M and grid[ii + dx][jj + dy]]
                flag = len(zero_num) <= 1 or (len(zero_num) == 2 and 1 in zero_num and (2 in zero_num))
                if grid[ii][jj] and flag:
                    done.add((ii, jj))
                    dfs(ii, jj, grid[ii][jj], done)
                    done.remove((ii, jj))
        return self.res
