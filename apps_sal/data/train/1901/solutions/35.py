DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def move(x, y):
            ans = []
            for mv_x, mv_y in DIRECTIONS:
                x_ = x + mv_x
                y_ = y + mv_y
                if 0 <= x_ < N and 0 <= y_ < N:
                    ans.append((x_, y_))
            return ans

        # return area of the island
        def dfs(x, y, idx):
            ans = 1
            grid[x][y] = idx
            for i, j in move(x, y):
                if grid[i][j] == 1:
                    ans += dfs(i, j, idx)
            return ans

        idx = 2
        areas = {0: 0}
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    areas[idx] = dfs(i, j, idx)
                    idx += 1

        ans = max(areas.values())
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    cands = set(grid[x][y] for x, y in move(i, j))
                    ans = max(ans, sum(areas[idx] for idx in cands) + 1)
        return ans
