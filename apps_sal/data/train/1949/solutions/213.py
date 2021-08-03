class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def q(g, i, j, t, s, vis):
            if i >= len(g) or j >= len(g[0]) or i < 0 or j < 0 or g[i][j] == 0 or vis[i][j] == 1:
                s[0] = max(s[0], t[0])

                return

            temp = g[i][j]
            g[i][j] = 0
            t[0] += temp
            q(g, i, j + 1, t, s, vis)
            q(g, i + 1, j, t, s, vis)
            q(g, i - 1, j, t, s, vis)
            q(g, i, j - 1, t, s, vis)
            t[0] -= temp
            g[i][j] = temp

        s = [0]
        t = [0]
        vis = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                t = [0]
                q(grid, i, j, t, s, vis)

        return s[0]
