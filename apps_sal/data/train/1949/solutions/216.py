class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = [0]

        def path(i, j, seen, val):
            ans[0] = max(ans[0], val)
            adjacent = [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]
            for (k, l) in adjacent:
                if k < 0 or k >= m or l < 0 or (l >= n):
                    continue
                if grid[k][l] != 0 and (k, l) not in seen:
                    path(k, l, seen + [(k, l)], val + grid[k][l])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    path(i, j, [(i, j)], grid[i][j])
        return max(ans)
