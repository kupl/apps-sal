class Piece:

    def __init__(self, map):
        self.map = map
        self.size = (len(map) - 1, len(map[0]) - 1)
        for num, line in enumerate(map):
            for tag in ('^', '<', 'v', '>'):
                if tag in line:
                    self.x, self.y, self.direct = num, line.index(tag), tag
        self.walked = set()     # 记录所有行进过得点
        self.walked.add((self.x, self.y))
        self.forks = []     # 记录所有岔路口以及在岔路口时的步数
        self.steps = 0  # 记录行动过得步数，方便回溯
        self.check_fork(self.x, self.y, 1)  # 起点时有两个方向就算岔路口
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
                if self.map[x_][y_] != '#':
                    count += 1
        fork = ((x, y), self.steps, self.direct)
        for _ in range(count - direct):   # 四个方向有三个能通才是岔路口
            self.forks.append(fork)

    def draw_map(self, x, y):
        self.map[x] = self.map[x][:y] + self.direct + self.map[x][y + 1:]

    def go_forward(self):
        self.direct, (x, y) = self.turn[self.direct]['F']
        x, y = self.x + x, self.y + y
        if self.map[x][y] != '#' and (x, y) not in self.walked:     # 只有前方是空地，并且没有走过才会向前走
            self.x, self.y = x, y
            self.walked.add((x, y))  # 将走过的路劲都记录下来，不走重复的路
            self.steps += 1
            self.check_fork(x, y)
            #self.draw_map(x, y)
            return 'F'
        else:   # 否则转向
            for key in ('L', 'R', 'B'):
                direct, (x, y) = self.turn[self.direct][key]
                x, y = self.x + x, self.y + y
                if self.map[x][y] != '#' and (x, y) not in self.walked:  # 转向时必须考虑转向后的方位没有走过且是空地
                    self.direct = direct
                    self.steps += 1
                    #self.draw_map(self.x, self.y)
                    return key
            if self.forks:     # 如果3个方向都不行，则检查是否能回溯，如果不能则返回None
                (self.x, self.y), self.steps, self.direct = self.forks.pop()
                return self.steps
            else:
                return None


def escape(maze):
    # Have a nice sleep ;)
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
