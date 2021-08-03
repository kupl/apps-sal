class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        def Check(i, j):
            ans = 1
            Dis = min(m - i, n - j)
            for k in range(max_dis, Dis):
                ok = True
                for h in range(i, i + k + 1):
                    if grid[h][j] == 0:
                        ok = False
                        break
                    if grid[h][j + k] == 0:
                        ok = False
                        break
                for h in range(j, j + k + 1):
                    if grid[i][h] == 0:
                        ok = False
                        break
                    if grid[i + k][h] == 0:
                        ok = False
                        break
                if ok:
                    ans = max(ans, (k + 1) * (k + 1))
            return ans

        m = len(grid)
        n = len(grid[0])
        max_so_far = 0
        max_dis = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and i + max_dis < m and j + max_dis < n:
                    max_so_far = max(max_so_far, Check(i, j))
                    max_dis = int(math.sqrt(max_so_far))
        return max_so_far
