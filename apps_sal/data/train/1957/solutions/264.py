class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid:
            return -1
        queue = collections.deque([(0, 0, 0)])
        visited = collections.defaultdict(int)
        visited[0, 0] = 0
        dist = 0
        while queue:
            for _ in range(len(queue)):
                (x, y, o) = queue.popleft()
                if o > k:
                    continue
                elif (x, y) == (len(grid) - 1, len(grid[0]) - 1):
                    return dist
                else:
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for direction in directions:
                        (dx, dy) = direction
                        if x + dx < 0 or x + dx >= len(grid) or y + dy < 0 or (y + dy >= len(grid[0])):
                            continue
                        if grid[x + dx][y + dy] == 1:
                            if o + 1 > k or ((x + dx, y + dy) in visited and o + 1 >= visited[x + dx, y + dy]):
                                continue
                            else:
                                queue.append((x + dx, y + dy, o + 1))
                                visited[x + dx, y + dy] = o + 1
                        elif o > k or ((x + dx, y + dy) in visited and o >= visited[x + dx, y + dy]):
                            continue
                        else:
                            queue.append((x + dx, y + dy, o))
                            visited[x + dx, y + dy] = o
            dist += 1
        return -1
