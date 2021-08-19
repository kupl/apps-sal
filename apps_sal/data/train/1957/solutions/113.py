class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        n, m = len(grid), len(grid[0])
        vis = set()
        vis.add((0, 0, 0))  # i,j,obstacleCount

        q = [(0, 0, 0, 0)]  # steps, i,j,obstacleCount

        def neighbors(i, j, oc):
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < m:
                    newoc = oc + grid[x][y]
                    if newoc <= k and (x, y, newoc) not in vis:
                        yield x, y, newoc

        while q:
            steps, i, j, obstacleCount = q.pop(0)

            if i == n - 1 and j == m - 1:
                return steps
            else:
                for x, y, oc in neighbors(i, j, obstacleCount):
                    vis.add((x, y, oc))
                    q.append((steps + 1, x, y, oc))

        return - 1
