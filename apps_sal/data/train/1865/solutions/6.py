class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:

        queue = deque()
        m = len(grid)
        n = len(grid[0])
        visited = {}

        rq = deque()
        reach = {}
        startx, starty = -1, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    rq.append([i, j])
                    startx, starty = i, j

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'B':
                    queue.append([i, j, 0, startx, starty])
                    visited[(i, j, startx, starty)] = 1

        while(len(queue) > 0):
            x, y, step, startx, starty = queue.popleft()

            if grid[x][y] == 'T':
                return step

            rq = deque()
            reach = {}
            rq.append([startx, starty])
            while(len(rq) > 0):
                rx, ry = rq.popleft()
                reach[(rx, ry)] = 1
                for deltax, deltay in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nx, ny = rx + deltax, ry + deltay
                    if nx >= 0 and nx < m and ny >= 0 and ny < n:
                        if grid[nx][ny] != '
                        rq.append([nx, ny])
                        reach[(nx, ny)] = 1

            for deltax, deltay in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = x + deltax, y + deltay
                otherx, othery = x - deltax, y - deltay

                if nx >= 0 and nx < m and ny >= 0 and ny < n and otherx >= 0 and otherx < m and othery >= 0 and othery < n:
                    if grid[nx][ny] != '
                    if (nx, ny, otherx, othery) not in visited and (otherx, othery) in reach:
                        queue.append([nx, ny, step + 1, otherx, othery])
                        visited[(nx, ny, otherx, othery)] = 1

        return -1
