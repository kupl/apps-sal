import collections


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # closed island point rules: (1) it must be 0 (2) it cannot be boundary
        #   (3) its nb either 1 or 0 (need to append) (4) all connected component follow this rule
        visited = set()
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited:
                    continue
                if grid[i][j] == 1:
                    continue
                tmp = self.bfs(grid, i, j, visited)
                # if tmp == 1:
                #print('found at %d, %d: %s' %(i, j, visited))
                res += tmp
        return res

    def bfs(self, grid, x, y, visited):
        # return 1 if this (BFS connected) is closed island, else 0
        visited.add((x, y))
        # now not boundary, do bfs
        res = 1
        q = collections.deque([(x, y)])
        while q:
            x, y = q.pop()
            if self.is_boundary(grid, x, y):
                res = 0  # not closed by water
            for newx, newy in self.get_nb(grid, x, y):
                if (newx, newy) in visited:
                    continue
                if grid[newx][newy] == 1:
                    continue  # closed by water, stop this direction
                if grid[newx][newy] == 0:
                    q.appendleft((newx, newy))
                    visited.add((newx, newy))
        return res

    def get_nb(self, grid, x, y):
        COOR = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        res = []
        for deltax, deltay in COOR:
            newx, newy = deltax + x, deltay + y
            if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]):
                res.append((newx, newy))
        return res

    def is_boundary(self, grid, x, y):
        if x == 0 or x == len(grid) - 1:
            return True
        if y == 0 or y == len(grid[0]) - 1:
            return True
        return False
