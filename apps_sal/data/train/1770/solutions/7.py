class Path:

    def __init__(self, maze, start, exit=None, pos='.'):
        self.maze = maze
        self.MAPd = {start: 1}
        self.exit = exit or (len(maze) - 1, len(maze[0]) - 1)
        self.grow = None
        self.pos = pos

    def run_maze(self):
        self.grow = self.len_
        for (x, floor) in enumerate(self.maze):
            for (y, _) in enumerate(floor):
                if self.maze[x][y] == self.pos and (not self.MAPd.get((x, y))):
                    self.mover(x, y, [])

    def mover(self, x, y, ways=[]):
        [not self.MAPd.get(e) or ways.append(self.MAPd[e]) for e in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))]
        if ways:
            self.MAPd[x, y] = min(ways) + 1

    @property
    def len_(self):
        return len(self.MAPd)

    @property
    def new_way_exist(self):
        return self.grow != self.len_

    @property
    def get_exit(self):
        return self.MAPd.get(self.exit, 1) - 1


def path_finder(maze):
    mazer = Path(maze.split('\n'), (0, 0))
    while mazer.new_way_exist:
        mazer.run_maze()
    return mazer.get_exit
