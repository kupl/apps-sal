class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        '''
        最短步数，利用BFS。有四种移动方式
        向右，向下，水平竖直
        '''
        n = len(grid)
        q = [(0, 0, 0, 1)]
        moves = 0
        visited = set([(0, 0, 0, 1)])
        while q:
            size = len(q)
            for _ in range(size):
                x1, y1, x2, y2 = q.pop(0)
                if x1 == n - 1 and y1 == n - 2 and x2 == n - 1 and y2 == n - 1:
                    return moves
                if y1 + 1 < n and grid[x1][y1 + 1] == 0 and y2 + 1 < n and grid[x2][y2 + 1] == 0:
                    if (x1, y1 + 1, x2, y2 + 1) not in visited:
                        visited.add((x1, y1 + 1, x2, y2 + 1))
                        q.append((x1, y1 + 1, x2, y2 + 1))
                if x1 + 1 < n and grid[x1 + 1][y1] == 0 and x2 + 1 < n and grid[x2 + 1][y2] == 0:
                    if ((x1 + 1, y1, x2 + 1, y2)) not in visited:
                        visited.add((x1 + 1, y1, x2 + 1, y2))
                        q.append((x1 + 1, y1, x2 + 1, y2))
                if x1 == x2 and y2 == y1 + 1 and x1 + 1 < n and grid[x1 + 1][y1] + grid[x1 + 1][y1 + 1] == 0:
                    if (x1, y1, x1 + 1, y1) not in visited:
                        visited.add((x1, y1, x1 + 1, y1))
                        q.append((x1, y1, x1 + 1, y1))
                if y1 == y2 and x2 == x1 + 1 and y1 + 1 < n and grid[x1][y1 + 1] + grid[x1 + 1][y1 + 1] == 0:
                    if (x1, y1, x1, y1 + 1) not in visited:
                        visited.add((x1, y1, x1, y1 + 1))
                        q.append((x1, y1, x1, y1 + 1))

            moves += 1
        return -1
