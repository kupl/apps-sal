class Piece:

    def __init__(self, map):
        self.map = map
        self.size = (len(map) - 1, len(map[0]) - 1)
        for num, line in enumerate(map):
            for tag in ('^', '<', 'v', '>'):
                if tag in line:
                    self.x, self.y, self.direct = num, line.index(tag), tag
        self.walked = set()
        self.walked.add((self.x, self.y))
        self.forks = []
        self.steps = 0
        self.check_fork(self.x, self.y, 1)
        self.dir = {
            'up': ('^', (-1, 0)),
            'down': ('v', (1, 0)),
            'left': ('<', (0, -1)),
            'right': ('>', (0, 1)),
        }
        self.turn = {
            '>': {'L': self.dir['up'], 'R': self.dir['down'], 'B': self.dir['left'], 'F': self.dir['right']},
            '<': {'L': self.dir['down'], 'R': self.dir['up'], 'B': self.dir['right'], 'F': self.dir['left']},
            '^': {'L': self.dir['left'], 'R': self.dir['right'], 'B': self.dir['down'], 'F': self.dir['up']},
            'v': {'L': self.dir['right'], 'R': self.dir['left'], 'B': self.dir['up'], 'F': self.dir['down']},
        }

    def check_fork(self, x, y, direct=2):
        count = 0
        for x_, y_ in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if x_ >= 0 and x_ <= self.size[0] and y_ >= 0 and y_ <= self.size[1]:
                if self.map[x_][y_] != '
                count += 1
        fork = ((x, y), self.steps, self.direct)
        for _ in range(count - direct):
            self.forks.append(fork)

    def draw_map(self, x, y):
        self.map[x] = self.map[x][:y] + self.direct + self.map[x][y + 1:]

    def go_forward(self):
        self.direct, (x, y) = self.turn[self.direct]['F']
        x, y = self.x + x, self.y + y
        if self.map[x][y] != '
        self.x, self.y = x, y
        self.walked.add((x, y))
        self.steps += 1
        self.check_fork(x, y)
        return 'F'
        else:
            for key in ('L', 'R', 'B'):
                direct, (x, y) = self.turn[self.direct][key]
                x, y = self.x + x, self.y + y
                if self.map[x][y] != '
                self.direct = direct
                self.steps += 1
                return key
            if self.forks:
                (self.x, self.y), self.steps, self.direct = self.forks.pop()
                return self.steps
            else:
                return None


def escape(maze):
    p = Piece(maze)
    res = ''

    while p.x not in (0, p.size[0]) and p.y not in (0, p.size[1]):
        tmp = p.go_forward()
        if tmp is None:
            return []
        elif isinstance(tmp, int):
            res = res[:tmp]
        else:
            res += tmp
    return list(res)
