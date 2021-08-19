import copy


class Solution:

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        (m, n) = (len(grid), len(grid[0]))
        tldr = [copy.deepcopy(grid) for _ in range(4)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if i:
                        tldr[0][i][j] = tldr[0][i - 1][j] + 1
                    if j:
                        tldr[1][i][j] = tldr[1][i][j - 1] + 1
        for j in range(n - 1, -1, -1):
            for i in range(m - 1, -1, -1):
                if grid[i][j]:
                    if i + 1 < m:
                        tldr[2][i][j] = tldr[2][i + 1][j] + 1
                    if j + 1 < n:
                        tldr[3][i][j] = tldr[3][i][j + 1] + 1
        mk = 0
        for i in range(m):
            for j in range(n):
                k0 = 0 if i == 0 or j == 0 else min(tldr[2][i - 1][j - 1], tldr[3][i - 1][j - 1])
                for k in range(min(tldr[2][i][j], tldr[3][i][j]) - 1, k0 - 1, -1):
                    if min(tldr[0][i + k][j + k], tldr[1][i + k][j + k]) >= k:
                        mk = max(mk, k + 1)
                        break
        return mk * mk
