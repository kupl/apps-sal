from collections import deque


class Solution:

    def minPushBox(self, grid: List[List[str]]) -> int:
        (m, n) = (len(grid), len(grid[0]))

        def Can(i, j):
            ss.add((i, j))
            for (x, y) in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n and ((x, y) not in ss) and (grid[x][y] == '.'):
                    Can(x, y)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    ppl = (i, j)
                    grid[i][j] = '.'
                elif grid[i][j] == 'B':
                    box = (i, j)
                    grid[i][j] = '.'
                elif grid[i][j] == 'T':
                    target = (i, j)
                    grid[i][j] = '.'
        visited = set()
        queue = deque()
        queue.append((box[0], box[1], 0, ppl[0], ppl[1]))
        ss = set()
        while queue:
            (x, y, count, p1, p2) = queue.popleft()
            if (x, y) == target:
                return count
            ss = {(x, y)}
            Can(p1, p2)
            if x + 1 < m and 0 <= x - 1 and (grid[x + 1][y] == '.') and (grid[x - 1][y] == '.'):
                if (x - 1, y, x, y) not in visited and (x - 1, y) in ss:
                    visited.add((x - 1, y, x, y))
                    queue.append((x + 1, y, count + 1, x - 1, y))
                if (x + 1, y, x, y) not in visited and (x + 1, y) in ss:
                    visited.add((x + 1, y, x, y))
                    queue.append((x - 1, y, count + 1, x + 1, y))
            if y + 1 < n and 0 <= y - 1 and (grid[x][y - 1] == '.') and (grid[x][y + 1] == '.'):
                if (x, y - 1, x, y) not in visited and (x, y - 1) in ss:
                    visited.add((x, y - 1, x, y))
                    queue.append((x, y + 1, count + 1, x, y - 1))
                if (x, y + 1, x, y) not in visited and (x, y + 1) in ss:
                    visited.add((x, y + 1, x, y))
                    queue.append((x, y - 1, count + 1, x, y + 1))
        return -1
