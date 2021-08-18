class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        self.empty = [['.' for _ in range(n)] for _ in range(m)]
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == 'B':
                    start = (i, j)
                if c == 'S':
                    player = (i, j)
                if c == 'T':
                    target = (i, j)
                if c == '
                self.empty[i][j] = '
        visit = [[0 for _ in range(n)] for _ in range(m)]
        visit[start[0]][start[1]] += 1
        deq = collections.deque([(start, player, (-1, -1))])
        push = 0
        while deq and push < m * n:
            sz = len(deq)
            for i in range(sz):
                box, player, previous = deq.popleft()
                if box == target:
                    return push
                cango = self.player(player, box, self.empty)
                for d in self.direction:
                    nr, nc = box[0] + d[0], box[1] + d[1]
                    pr, pc = box[0] + d[2], box[1] + d[3]
                    if 0 <= nr < m and 0 <= nc < n and 0 <= pr < m and 0 <= pc < n:
                        if (self.empty[nr][nc] == '.') and cango[pr][pc] and visit[nr][nc] < 2:
                            visit[nr][nc] += 1
                            deq.append(((nr, nc), (pr, pc), box))
            push += 1
        return -1

    def player(self, player, box, grid):
        m, n = len(grid), len(grid[0])
        visit = [[False for _ in range(n)] for _ in range(m)]
        visit[player[0]][player[1]] = True
        deq = collections.deque([player])
        while deq:
            sz = len(deq)
            for i in range(sz):
                cur = deq.popleft()
                for d in self.direction:
                    nr, nc = cur[0] + d[0], cur[1] + d[1]
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '.' and not visit[nr][nc] and box != (nr, nc):
                        visit[nr][nc] = True
                        deq.append((nr, nc))
        return visit

    def __init__(self):
        self.direction = ((0, 1, 0, -1), (0, -1, 0, 1), (1, 0, -1, 0), (-1, 0, 1, 0))
        self.empty = None
