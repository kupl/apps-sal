class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dfs(i, j, vis):
            res = 0
            for (z1, z2) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                (x, y) = (i + z1, j + z2)
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and ((x, y) not in vis) and (grid[x][y] != 0):
                    vis.add((x, y))
                    res = max(res, dfs(x, y, vis))
                    vis.remove((x, y))
            return res + grid[i][j]

        def check(i, j):
            if i == 0 or j == 0 or i == len(grid) - 1 or (j == len(grid[0]) - 1):
                return True
            cnt = 0
            for (z1, z2) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                (x, y) = (i + z1, j + z2)
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (grid[x][y] != 0):
                    cnt += 1
            if cnt <= 1:
                return True
            return False
        res = 0
        if not grid or not grid[0]:
            return res
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0 and check(i, j):
                    vis = set()
                    vis.add((i, j))
                    ans = dfs(i, j, vis)
                    res = max(res, ans)
        return res
