class Solution(object):

    def shortestPath(self, grid, k):
        k -= grid[0][0] == 1
        if k < 0:
            return -1
        (n, m) = (len(grid), len(grid[0]))
        if k >= m + n - 3:
            return m + n - 2
        (n, m) = (n - 1, m - 1)
        bfs = [(0, 0, k)]
        seen = set()
        steps = 0
        while bfs:
            nxt = []
            for (i, j, rem) in bfs:
                if (i, j, rem) in seen:
                    continue
                if i == n and j == m:
                    return steps
                if i > 0:
                    nrem = rem - (grid[i - 1][j] == 1)
                    if nrem >= 0:
                        nxt.append((i - 1, j, nrem))
                if j > 0:
                    nrem = rem - (grid[i][j - 1] == 1)
                    if nrem >= 0:
                        nxt.append((i, j - 1, nrem))
                if i < n:
                    nrem = rem - (grid[i + 1][j] == 1)
                    if nrem >= 0:
                        nxt.append((i + 1, j, nrem))
                if j < m:
                    nrem = rem - (grid[i][j + 1] == 1)
                    if nrem >= 0:
                        nxt.append((i, j + 1, nrem))
                seen.add((i, j, rem))
            steps += 1
            bfs = nxt
        return -1
