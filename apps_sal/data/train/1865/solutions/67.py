class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        free = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'T':
                    tx, ty = i, j
                    free.add((i, j))
                if grid[i][j] == 'S':
                    sx, sy = i, j
                    free.add((i, j))
                if grid[i][j] == 'B':
                    bx, by = i, j
                    free.add((i, j))
                if grid[i][j] == '.':
                    free.add((i, j))
        pq = [(0, sx, sy, bx, by)]
        visited = set()
        direction = [(0,1), (1,0), (-1,0), (0,-1)]
        while pq:
            moves, sx, sy, bx, by = heapq.heappop(pq)
            if bx == tx and by == ty:
                return moves
            if (sx, sy, bx, by) in visited:
                continue
            visited.add((sx, sy, bx, by))
            for d in direction:
                dx, dy = d
                if sx + dx == bx and sy + dy == by and (bx + dx, by + dy) in free:
                    heapq.heappush(pq, (moves + 1, sx + dx, sy + dy, bx + dx, by + dy))
                if (sx + dx, sy + dy) in free and (sx + dx, sy + dy) != (bx, by) and (sx + dx, sy + dy, bx, by) not in visited:
                    heapq.heappush(pq, (moves, sx + dx, sy + dy, bx, by))
        return -1
