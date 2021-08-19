class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        def move(pos_x, pos_y, obs, steps):
            if pos_x < 0 or pos_x >= len(grid) or pos_y < 0 or (pos_y >= len(grid[0])):
                return
            if grid[pos_x][pos_y] == 1:
                if obs == 0:
                    return
                obs -= 1
            if self.memo.get((pos_x, pos_y, obs), 2000) <= steps:
                return
            self.memo.update({(pos_x, pos_y, obs): steps})
            q.append((pos_x, pos_y, obs, steps))
            if pos_x == len(grid) - 1 and pos_y == len(grid[0]) - 1:
                self.ans = steps
        self.ans = None
        q = deque([(0, 0, k, 0)])
        self.memo = {(0, 0, k): 0}
        while q:
            (pos_x, pos_y, obs, steps) = q.popleft()
            if pos_x == len(grid) - 1 and pos_y == len(grid[0]) - 1:
                return steps
            move(pos_x - 1, pos_y, obs, steps + 1)
            move(pos_x + 1, pos_y, obs, steps + 1)
            move(pos_x, pos_y - 1, obs, steps + 1)
            move(pos_x, pos_y + 1, obs, steps + 1)
            if self.ans is not None:
                return self.ans
        return -1
