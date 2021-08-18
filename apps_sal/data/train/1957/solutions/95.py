class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()

        def bfs(steps, x, y, oc):
            visited.add((x, y, oc))
            q = collections.deque()
            q.append((steps, x, y, oc))
            while q:
                (steps, r, c, obstacleCount) = q.popleft()
                if r == m - 1 and c == n - 1:
                    return steps
                for (i, j, oc) in getneighbors(r, c, obstacleCount):
                    if (i, j, oc) not in visited:
                        visited.add((i, j, oc))
                        q.append((steps + 1, i, j, oc))
            return -1

        def getneighbors(x, y, oc):
            result = []
            for (x, y) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= x < m and 0 <= y < n:
                    newoc = oc + grid[x][y]
                    if grid[x][y] == 0 or (grid[x][y] == 1 and newoc <= k):
                        yield (x, y, newoc)

            return result
        return bfs(0, 0, 0, 0)
