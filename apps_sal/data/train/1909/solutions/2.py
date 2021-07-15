class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        h = [row[:] for row in grid]
        v = [row[:] for row in grid]
        for row in range(m):
            for col in range(1, n):
                if h[row][col] != 0:
                    h[row][col] += h[row][col-1]
        for col in range(n):
            for row in range(1, m):
                if v[row][col] != 0:
                    v[row][col] += v[row-1][col]
        for row in range(m):
            for col in range(n):
                curr = grid[row][col]
                if not curr: continue
                side = h[row][col] if h[row][col] < v[row][col] else v[row][col]
                res = 1
                for x in range(side, 0, -1):
                    if v[row][col-x+1] >= x and h[row-x+1][col] >= x:
                        res = x*x
                        break
                if res > ans:
                    ans = res
        return ans
