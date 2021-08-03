class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        seen = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
        queue = collections.deque([(0, 0, 0)])
        step = 0
        direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            length = len(queue)
            for _ in range(length):
                x, y, u = queue.popleft()
                if x == len(grid) - 1 and y == len(grid[0]) - 1:
                    return step
                if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1:
                    continue
                if grid[x][y] == 1:
                    u += 1
                if u > k or u >= seen[x][y]:
                    continue
                seen[x][y] = u
                for i, j in direct:
                    queue.append((x + i, y + j, u))
            step += 1
        return -1
