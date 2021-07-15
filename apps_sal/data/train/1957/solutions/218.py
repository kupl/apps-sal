class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        min_d = [[math.inf for i in range(n)] for j in range(m)]
        min_d[0][0] = 0
        todo = collections.deque()
        todo.append((0, 0, 0))
        def adjust():
            while todo:
                x, y, d = todo.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and min_d[nx][ny] > d + 1:
                        min_d[nx][ny] = d + 1
                        todo.append((nx, ny, d + 1))
        adjust()
        
        blockes = []
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    blockes.append((x, y))
        min_d_to_block = {}
        
        for i in range(k):
            delay_update = []
            for x, y in blockes:
                d = math.inf
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and min_d[nx][ny] != math.inf:
                        d = min(d, min_d[nx][ny] + 1)
                if min_d[x][y] > d:
                    delay_update.append((x, y, d))
                    todo.append((x, y, d))
            for x, y, d in delay_update:
                min_d[x][y] = d
            delay_update = []
            adjust()
            
        return -1 if min_d[m-1][n-1] == inf else min_d[m-1][n-1]
