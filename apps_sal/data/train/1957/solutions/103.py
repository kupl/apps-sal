class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q, nq, d = set([(0, 0)]), set(), {(0, 0): (0, 0)}
        while q:
            for i, j in q:
                dist, obst = d[(i, j)]
                for m, n in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                    if 0 <= m < len(grid) and 0 <= n < len(grid[0]):
                        if obst + grid[m][n] < d.get((m, n), (0, float('inf')))[1]:
                            d[(m, n)] = (dist + 1, obst + grid[m][n])
                            nq.add((m, n))
                dist, obst = d.get((len(grid) - 1, len(grid[0]) - 1), (0, float('inf')))
                if obst <= k:
                    return dist
            q, nq = nq, set()
        return -1
