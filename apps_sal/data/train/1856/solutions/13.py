class Solution:

    def is_empty(self, xy):
        if 0 <= xy[0] < self.m and 0 <= xy[1] < self.n:
            return self.grid[xy[0]][xy[1]] == 0
        else:
            return False

    def next_positions(self, pos):
        (tail, head) = pos
        if tail[0] == head[0]:
            if self.is_empty((head[0], head[1] + 1)):
                yield (head, (head[0], head[1] + 1))
            if self.is_empty((tail[0] + 1, tail[1])) and self.is_empty((head[0] + 1, head[1])):
                yield ((tail[0] + 1, tail[1]), (head[0] + 1, head[1]))
                yield (tail, (tail[0] + 1, tail[1]))
        else:
            assert tail[1] == head[1]
            if self.is_empty((head[0] + 1, head[1])):
                yield (head, (head[0] + 1, head[1]))
            if self.is_empty((tail[0], tail[1] + 1)) and self.is_empty((head[0], head[1] + 1)):
                yield ((tail[0], tail[1] + 1), (head[0], head[1] + 1))
                yield (tail, (tail[0], tail[1] + 1))

    def minimumMoves(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        layer = {((0, 0), (0, 1))}
        visited = set()
        dist = 0
        target = ((self.m - 1, self.n - 2), (self.m - 1, self.n - 1))
        while layer:
            if target in layer:
                return dist
            visited |= layer
            next_layer = set()
            for pos in layer:
                for next_pos in self.next_positions(pos):
                    if next_pos not in visited:
                        next_layer.add(next_pos)
            layer = next_layer
            dist += 1
        return -1
