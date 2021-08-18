from collections import deque


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:

        def can_reach(x, y):
            q = deque([x])
            seen = set([x])
            while q:
                i, j = q.popleft()
                if (i, j) == y:
                    return True
                for di, dj in (-1, 0), (1, 0), (0, 1), (0, -1):
                    i_ = i + di
                    j_ = j + dj
                    if 0 <= i_ < m and 0 <= j_ < n and (i_, j_) not in seen and grid[i_][j_] == '.':
                        seen.add((i_, j_))
                        q.append((i_, j_))
            return False

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'T':
                    t = (i, j)
                    grid[i][j] = '.'
                if grid[i][j] == 'B':
                    b = (i, j)
                    grid[i][j] = '.'
                if grid[i][j] == 'S':
                    s = (i, j)
                    grid[i][j] = '.'
        depth = 0
        q = deque([(b, s)])
        seen = set([(b, s)])

        while q:
            depth += 1
            for _ in range(len(q)):
                b, s = q.popleft()
                grid[b[0]][b[1]] = 'B'
                for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
                    x, y = b[0] + dx, b[1] + dy
                    bx, by = b[0] - dx, b[1] - dy

                    if 0 <= x < m and 0 <= y < n and 0 <= bx < m and 0 <= by < n and grid[x][y] != '
                    seen.add(((bx, by), b))
                    q.append(((bx, by), b))
                    if (bx, by) == t:
                        return depth
                grid[b[0]][b[1]] = '.'
        return -1
