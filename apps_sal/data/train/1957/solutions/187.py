class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (m, n) = (len(grid), len(grid[0]))

        def get_neighbors(i, j):
            neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            return [(x, y) for (x, y) in neighbors if x >= 0 and x <= m - 1 and (y >= 0) and (y <= n - 1)]
        visited = set()
        frontier = deque([(0, 0, 0)])
        level = 0
        while len(frontier) > 0:
            for i in range(len(frontier)):
                (x, y, obs) = frontier.popleft()
                if x == m - 1 and y == n - 1:
                    return level
                if (x, y, obs) not in visited:
                    neighbors = get_neighbors(x, y)
                    if grid[x][y] == 1:
                        if obs == k:
                            continue
                        else:
                            frontier.extend([(x, y, obs + 1) for (x, y) in neighbors])
                    else:
                        frontier.extend([(x, y, obs) for (x, y) in neighbors])
                    visited.add((x, y, obs))
            level += 1
        return -1
