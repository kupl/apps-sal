class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(p1, p2, t1, t2, b1, b2):
            visited = visited = [[False for _ in range(n)] for _ in range(m)]
            queue = collections.deque()
            queue.append((p1, p2))
            visited[p1][p2] = True

            while queue:
                x, y = queue.popleft()
                if (x, y) == (t1, t2):
                    return True
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if visited[nx][ny]:
                            continue
                        if (nx, ny) == (t1, t2):
                            return True
                        if (nx, ny) != (b1, b2) and grid[nx][ny] != '
                           queue.append((nx, ny))
                            visited[nx][ny] = True
            return False

        def inbound(x, y):
            return 0 <= x < m and 0 <= y < n

        for i in range(m):
            for j in range(n):
                if grid[i][j] != '
                   if grid[i][j] == 'S':
                        player = (i, j)
                    elif grid[i][j] == 'B':
                        box = (i, j)
                    elif grid[i][j] == 'T':
                        end = (i, j)
        p1, p2 = player
        b1, b2 = box
        e1, e1 = end

        visited = set()
        step = -1

        queue = collections.deque()
        queue.append((b1, b2, p1, p2))

        while queue:
            step += 1
            for _ in range(len(queue)):
                x, y, p1, p2 = queue.popleft()
                if inbound(x - 1, y) and inbound(x + 1, y) and grid[x + 1][y] != '
                   if (x - 1, y, x, y) not in visited:
                        if grid[x - 1][y] != '
                           if grid[x - 1][y] == 'T':
                                return step + 1
                            else:
                                queue.append((x - 1, y, x, y))
                                visited.add((x - 1, y, x, y))
                                visited.add((x, y, x + 1, y))
                if inbound(x - 1, y) and inbound(x + 1, y) and grid[x - 1][y] != '
                   if (x + 1, y, x, y) not in visited:
                        if grid[x + 1][y] != '
                           if grid[x + 1][y] == 'T':
                                return step + 1
                            else:
                                queue.append((x + 1, y, x, y))
                                visited.add((x + 1, y, x, y))
                                visited.add((x, y, x - 1, y))

                if inbound(x, y + 1) and inbound(x, y - 1) and grid[x][y + 1] != '
                   if (x, y - 1, x, y) not in visited:
                        if grid[x][y - 1] != '
                           if grid[x][y - 1] == 'T':
                                return step + 1
                            else:
                                queue.append((x, y - 1, x, y))
                                visited.add((x, y - 1, x, y))
                                visited.add((x, y, x, y + 1))

                if inbound(x, y + 1) and inbound(x, y - 1) and grid[x][y - 1] != '
                   if (x, y + 1, x, y) not in visited:
                        if grid[x][y + 1] != '
                           if grid[x][y + 1] == 'T':
                                return step + 1
                            else:
                                queue.append((x, y + 1, x, y))
                                visited.add((x, y + 1, x, y))
                                visited.add((x, y, x, y - 1))

        return -1
