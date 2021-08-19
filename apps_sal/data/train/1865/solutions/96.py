class Solution:
    def init_positions(self):
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 'S':
                    pusher = i, j
                if self.grid[i][j] == 'B':
                    box = i, j
                if self.grid[i][j] == 'T':
                    target = i, j
        return pusher, box, target

    def bfs_from_pusher(self, pusher, box):
        visited = set()
        frontier = {pusher}
        while frontier:
            visited |= frontier
            new_frontier = set()
            for pos in frontier:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_x, new_y = pos[0] + dx, pos[1] + dy
                    if (0 <= new_x < self.m and 0 <= new_y < self.n
                        and self.grid[new_x][new_y] != '#' and (new_x, new_y) != box
                            and (new_x, new_y) not in visited):
                        new_frontier.add((new_x, new_y))
            frontier = new_frontier
        return visited

    def reachable_neighbors_of(self, box, visited):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = box[0] + dx, box[1] + dy
            if (new_x, new_y) in visited:
                mir_x, mir_y = (2 * box[0] - new_x), (2 * box[1] - new_y)
                if 0 <= mir_x < self.m and 0 <= mir_y < self.n and self.grid[mir_x][mir_y] != '#':
                    yield mir_x, mir_y

    def minPushBox(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        pusher, box, target = self.init_positions()

        frontier = {(box, pusher)}
        visited = set()
        dist = 0
        while frontier:
            visited |= frontier
            for box, _ in visited:
                if box == target:
                    return dist

            new_frontier = set()
            for cur_box, cur_pusher in frontier:
                visited_pusher = self.bfs_from_pusher(cur_pusher, cur_box)
                for new_box in self.reachable_neighbors_of(cur_box, visited_pusher):
                    if (new_box, cur_box) not in visited:
                        new_frontier.add((new_box, cur_box))
            frontier = new_frontier
            dist += 1
        return -1
