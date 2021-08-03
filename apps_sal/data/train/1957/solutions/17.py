class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # BFS
        m, n = len(grid), len(grid[0])
        initial_state = (0, 0, k)  # (i, j, remaining obstacle elimination ability)
        q = collections.deque()
        q.append(initial_state)
        visited = set()
        visited.add(initial_state)
        dist = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        while q:
            for _ in range(len(q)):
                i, j, r = q.popleft()
                if r < 0:
                    continue
                if i == m - 1 and j == n - 1:
                    return dist
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 0:
                            next_state = (nx, ny, r)
                        else:
                            next_state = (nx, ny, r - 1)
                        if next_state not in visited:
                            q.append(next_state)
                            visited.add(next_state)

            dist += 1

        return -1
