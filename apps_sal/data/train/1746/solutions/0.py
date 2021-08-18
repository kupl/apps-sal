def rpg(field, actions):
    p = Player(field)
    try:
        for m in actions:
            if m == 'A':
                p.attack()
            elif m in 'HCK':
                p.use(m)
            elif m in '<^>v':
                p.rotate(m)
            p.checkDmgsAndAlive()
            if m == 'F':
                p.move()

    except Exception as e:
        return None
    return p.state()


class Player:
    DIRS = dict(list(zip('<>^v', ((0, -1), (0, 1), (-1, 0), (1, 0)))))

    def __init__(self, field):
        self.h, self.atk, self.d, self.bag, self.xps = 3, 1, 1, [], 0
        self.field = field
        self.pngs = {}
        for x, r in enumerate(self.field):
            for y, c in enumerate(r):
                if c in self.DIRS:
                    self.x, self.y, self.c = x, y, c
                    self.dx, self.dy = self.DIRS[c]
                elif c == 'D':
                    self.pngs[(x, y)] = {'h': 10, 'atk': 3}
                elif c == 'E':
                    self.pngs[(x, y)] = {'h': 1, 'atk': 2}
                elif c == 'M':
                    self.pngs['M'] = {'coins': 3}

    def state(self): return self.field, self.h, self.atk, self.d, sorted(self.bag)

    def rotate(self, c):
        self.dx, self.dy = self.DIRS[c]
        self.c = self.field[self.x][self.y] = c

    def move(self):
        self.field[self.x][self.y] = ' '
        self.x += self.dx
        self.y += self.dy
        c = self.field[self.x][self.y]
        assert c not in '
        if c != ' ':
            self.takeThis(c)
        self.field[self.x][self.y] = self.c

    def checkAhead(self, what):
        x, y = self.x + self.dx, self.y + self.dy
        assert self.field[x][y] in what
        return x, y

    def takeThis(self, c):
        if c not in 'SX':
            self.bag.append(c)
        if c == 'S':
            self.d += 1
        elif c == 'X':
            self.atk += 1

    def use(self, c):
        self.bag.remove(c)
        if c == 'C':
            x, y = self.checkAhead('M')
            self.pngs['M']['coins'] -= 1
            if not self.pngs['M']['coins']:
                self.field[x][y] = ' '
        elif c == 'H':
            assert self.h < 3
            self.h = 3
        elif c == 'K':
            x, y = self.checkAhead('|-')
            self.field[x][y] = ' '

    def attack(self):
        x, y = nmy = self.checkAhead('ED')
        self.pngs[nmy]['h'] -= self.atk
        if self.pngs[nmy]['h'] < 1:
            del self.pngs[nmy]
            self.field[x][y] = ' '
            lvlUp, self.xps = divmod(self.xps + 1, 3)
            self.atk += lvlUp

    def checkDmgsAndAlive(self):
        for dx, dy in list(self.DIRS.values()):
            nmy = self.x + dx, self.y + dy
            if nmy in self.pngs:
                self.h -= max(0, self.pngs[nmy]['atk'] - self.d)
                assert self.h > 0
