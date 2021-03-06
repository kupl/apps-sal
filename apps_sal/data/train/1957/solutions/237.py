class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid:
            return -1
        (m, n) = (len(grid), len(grid[0]))
        visited = defaultdict(int)
        (q, nq, step) = (deque([(0, 0, k)]), deque(), 0)
        while q:
            (x, y, chance) = q.popleft()
            if (x, y) == (m - 1, n - 1):
                return step
            for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                (xx, yy) = (x + dx, y + dy)
                if 0 <= xx < m and 0 <= yy < n:
                    chance_left = chance - grid[xx][yy]
                    if chance_left < 0:
                        continue
                    if (xx, yy) not in visited or visited[xx, yy] < chance_left:
                        visited[xx, yy] = chance_left
                        nq.append((xx, yy, chance_left))
            if not q:
                (q, nq) = (nq, deque())
                step += 1
        return -1
