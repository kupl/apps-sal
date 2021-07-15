class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        seen = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
        seen[0][0] = 0
        queue = collections.deque([(0, 0, 0)])
        step = 0
        direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            length = len(queue)
            for _ in range(length):
                x, y, u = queue.popleft()
                if x == len(grid) - 1 and y == len(grid[0]) - 1:
                    return step
                for i, j in direct:
                    newx, newy, newu = i + x, y + j, u
                    if newx < 0 or newy < 0 or newx > len(grid) - 1 or newy > len(grid[0]) - 1:
                        continue
                    if grid[newx][newy] == 1:
                        newu += 1
                    if newu > k or newu >= seen[newx][newy]:
                        continue
                    seen[newx][newy] = newu
                    queue.append((newx, newy, newu))
            step += 1
        return -1
