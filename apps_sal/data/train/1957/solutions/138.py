class Solution:
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return -1
        (n, m) = (len(grid), len(grid[0]))
        queue = deque()
        queue.append((0, 0, k))
        visited = set()
        visited.add((0, 0, k))
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                (i, j, chances) = queue.popleft()
                if i == n - 1 and j == m - 1:
                    return step
                for d in Solution.dirs:
                    (x, y) = (i + d[0], j + d[1])
                    if x < 0 or x >= n or y < 0 or (y >= m):
                        continue
                    if grid[x][y] == 0:
                        if (x, y, chances) not in visited:
                            queue.append((x, y, chances))
                            visited.add((x, y, chances))
                    elif grid[x][y] == 1:
                        if chances == 0:
                            continue
                        if (x, y, chances - 1) not in visited:
                            queue.append((x, y, chances - 1))
                            visited.add((x, y, chances - 1))
            step += 1
        return -1
