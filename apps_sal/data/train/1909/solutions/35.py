class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                l = (grid[i][j - 1] & 0xff if j else 0) + 1
                u = ((grid[i - 1][j] >> 8) & 0xff if i else 0) + 1
                grid[i][j] = u << 8 | l
                s = 1
                for k in reversed(list(range(min(l, u)))):
                    if (grid[i][j - k] >> 8) > k and (grid[i - k][j] & 0xff) > k:
                        s = k + 1
                        break
                result = max(result, s * s)
        return result
