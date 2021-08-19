class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        this_layer, next_layer = 1, 0
        reached = False
        cost = 0

        visited = [[-1] * len(grid[0]) for _ in range(len(grid))]
        visited[0][0] = k
        q = deque([(0, 0, k)])
        while q:
            r, c, p = q.popleft()
            if r == len(grid) - 1 and c == len(grid[0]) - 1 and grid[r][c] != 1:
                reached = True
                break
            for i in range(4):
                x, y = c + dx[i], r + dy[i]
                if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
                    continue
                if p - grid[y][x] <= visited[y][x]:  # have visited here on a better path.
                    continue
                q.append((y, x, p - grid[y][x]))
                visited[y][x] = p - grid[y][x]
                next_layer += 1
            this_layer -= 1
            if this_layer == 0:
                this_layer = next_layer
                next_layer = 0
                cost += 1

        if not reached:
            return -1
        return cost
