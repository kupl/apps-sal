class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        import queue
        queue = queue.Queue()
        queue.put((0, 0, k))
        visited = set([(0, 0, k)])

        steps = 0
        while not queue.empty():
            size = queue.qsize()
            for _ in range(size):
                x, y, c = queue.get()
                # print(x, y)
                if x == m - 1 and y == n - 1:
                    return steps
                for delta_x, delta_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x_, y_ = x + delta_x, y + delta_y
                    # print(x_, y_)
                    if x_ < 0 or x_ >= m or y_ < 0 or y_ >= n:
                        continue
                    if grid[x_][y_] == 1 and c > 0 and (x_, y_, c - 1) not in visited:
                        queue.put((x_, y_, c - 1))
                        visited.add((x_, y_, c - 1))
                    if grid[x_][y_] == 0 and (x_, y_, c) not in visited:
                        queue.put((x_, y_, c))
                        visited.add((x_, y_, c))
            steps += 1

        return -1
