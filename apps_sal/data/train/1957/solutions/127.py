class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = deque()
        queue.append((0, 0, k, 0))
        visited = set((0, 0, k))
        count = 0
        while queue:
            x, y, obstacles, steps = queue.popleft()
            visited.add((x, y, obstacles))

            for dx, dy in directions:
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                    if grid[x + dx][y + dy] == 0 and (x + dx, y + dy, obstacles) not in visited:
                        if x + dx == len(grid) - 1 and y + dy == len(grid[0]) - 1:
                            return steps + 1
                        queue.append((x + dx, y + dy, obstacles, steps + 1))
                        visited.add((x + dx, y + dy, obstacles))

                    if grid[x + dx][y + dy] == 1 and obstacles > 0 and (x + dx, y + dy, obstacles - 1) not in visited:
                        queue.append((x + dx, y + dy, obstacles - 1, steps + 1))
                        visited.add((x + dx, y + dy, obstacles - 1))

        return -1
