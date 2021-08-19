class Solution:

    def minPushBox(self, grid) -> int:
        T = B = S = (-1, -1)
        l = len(grid)
        w = len(grid[0])
        for i in range(l):
            for j in range(w):
                if grid[i][j] == 'T':
                    T = (i, j)
                elif grid[i][j] == 'B':
                    B = (i, j)
                elif grid[i][j] == 'S':
                    S = (i, j)
        directions = [0, -1, 0, 1, 0]
        q = [B + S]
        visited = set()
        steps = 0
        self.next_step = (-1, -1, -1, -1)

        def is_pushable(cur_bs, dx, dy):
            (bx, by, sx, sy) = cur_bs
            nbx = bx + dx
            nby = by + dy
            nsx = bx - dx
            nsy = by - dy
            if is_valid(nbx, nby) and is_valid(nsx, nsy):
                if is_reachable(sx, sy, nsx, nsy, bx, by):
                    self.next_step = (nbx, nby, nsx, nsy)
                    return True
            return False

        def is_valid(nx, ny):
            return 0 <= nx < l and 0 <= ny < w and (grid[nx][ny] != '#')

        def is_reachable(sx, sy, nsx, nsy, cur_bx, cur_by):
            queue = [(sx, sy)]
            visited_set = set()
            while queue:
                cur_s = queue.pop(0)
                if cur_s not in visited_set and cur_s != (cur_bx, cur_by):
                    visited_set.add(cur_s)
                    if cur_s == (nsx, nsy):
                        return True
                    (cx, cy) = cur_s
                    for idx in range(4):
                        (dx, dy) = (directions[idx], directions[idx + 1])
                        (nx, ny) = (cx + dx, cy + dy)
                        if is_valid(nx, ny):
                            queue.append((nx, ny))
            return False
        while q:
            tmp = []
            for cur in q:
                if cur not in visited:
                    visited.add(cur)
                    for i in range(4):
                        (dir_x, dir_y) = (directions[i], directions[i + 1])
                        if is_pushable(cur, dir_x, dir_y):
                            (box_x, box_y, _, _) = self.next_step
                            if (box_x, box_y) == T:
                                return steps + 1
                            tmp.append(self.next_step)
            q = tmp
            steps += 1
        return -1
