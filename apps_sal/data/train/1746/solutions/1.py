only_show_wrong()


class RPG:

    def __init__(self, field, actions):
        frame = ['
        self.field = [frame] + [['
        self.actions = actions
        self.l = len(self.field)
        self.pack = {'H': 3, 'X': 1, 'S': 1, }
        self.bag = []
        self.moves = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
        self.x = self.find_player(self.field, lambda e: any(('<' in e, '>' in e, '^' in e, 'v' in e)))
        self.y=self.find_player(self.field[self.x], lambda e: e in '<>^v')
        self._player=self.field[self.x][self.y]
        self.back=None
        self.boss=10
        self._result=1
        self.use_coint=0
        self.level_up=0
        self.ready_atack=[]
        self.use_item={'K': self.use_key, 'C': self.coint_act, 'H': self.get_energy, 'A': self.atack}

    def __call__(self):
        for i, act in enumerate(self.actions):
            self.use_item.get(act, self.make_step)(act, act != 'F')
            if not self._result:
                break
            self.enemy_status(i, act)
        if self.use_coint:
            x, y=self.step
            if self.field[x][y] != 'M':
                return
        return self.result

    @ property
    def game_over(self):
        self._result=None

    @ property
    def step(self):
        move=self.moves[self._player]
        return (self.x + move[0], self.y + move[1])

    @ property
    def result(self):
        if self._result:
            return ([line[1:-1] for line in self.field[1:-1]], *self.pack.values(), sorted(self.bag))

    @ property
    def set_player(self):
        self._player=self.field[self.x][self.y]
        return self._player

    def enemy_status(self, i, act):
        for x, y in [(self.x + 1, self.y), (self.x - 1, self.y), (self.x, self.y + 1), (self.x, self.y - 1)]:
            if self.field[x][y] in 'DE':
                self.ready_atack.append(self.field[x][y])
        if self.ready_atack:
            pref_a, next_a, l=self.actions, self.actions, len(self.actions) - 1
            if i and i < l and pref_a[i - 1] in '<>^vF' and next_a[i + 1] == 'F' and act == 'F' or act in '<>^vAH' and i != l or act == 'F' and i < l and next_a[i + 1] in '<>v^':
                self.enemy_atack()
            self.ready_atack=[]

    def enemy_atack(self):
        for enemy in self.ready_atack:
            self.pack['H'] -= max(0, (2, 3)[enemy == 'D'] - self.pack['S'])
            if self.pack['H'] <= 0:
                self.game_over

    def act(self):
        if self.back in '|-M
            self.game_over
        if self.back in 'KCH':
            self.bag.append(self.back)
        if self.back in 'SX':
            self.pack[self.back] += 1

    def ded(self, x, y):
        self.field[x][y]=' '

    def use_key(self, key, x):
        x, y=self.step
        if key in self.bag and self.field[x][y] in '|-':
            self.drop(key)
            self.ded(x, y)
        else:
            self.game_over

    def atack(self, x, z):
        x, y=self.step
        if self.field[x][y] == 'E':
            self.ded(x, y)
            self.level_up += 1
            if self.level_up == 3:
                self.pack['X'] += 1
                self.level_up=0
        elif self.field[x][y] == 'D':
            self.boss -= self.pack['X']
            if self.boss <= 0:
                self.ded(x, y)
        else:
            self.game_over

    def coint_act(self, coint, i):
        if coint not in self.bag:
            self.game_over
            return
        self.use_coint += i
        self.drop(coint)
        if self.use_coint == 3:
            x, y=self.step
            if self.field[x][y] == 'M':
                self.use_coint=0
                self.ded(x, y)
            else:
                self.game_over

    def get_energy(self, energy, x):
        if energy not in self.bag or self.pack[energy] >= 3:
            self.game_over
            return
        self.drop(energy)
        self.pack[energy]=3

    def drop(self, element):
        del self.bag[self.bag.index(element)]

    def make_step(self, element, p):
        way=(self.set_player, element)[p]
        if not p:
            self.field[self.x][self.y]=' '
            self.x, self.y=self.step
        if self.x < 1 or self.x >= self.l - 1 or self.y < 1 or self.y >= len(self.field[self.x]) - 1:
            self.game_over
            return
        if self.field[self.x][self.y] != ' ':
            self.back=self.field[self.x][self.y]
            self.act()
        self.field[self.x][self.y]=way
        self.set_player

    @ staticmethod
    def find_player(field, condition):
        return next(i for i, e in enumerate(field) if condition(e))


def rpg(f, a) -> Tuple[List[List[str]], int, int, int, List[str]]:
    play_game=RPG(f, a)
    return play_game()
