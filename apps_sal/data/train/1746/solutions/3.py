only_show_wrong()


def rpg(game: List[List[str]], actions: List[str]) -> Tuple[List[List[str]], int, int, int, List[str]]:

    class GameObject:
        def __init__(self, game, h, a, d, l=None):
            self.g = game
            self.l = l if l is not None else (0, 0)
            self.h = h
            self.a = a
            self.d = d

        @property
        def is_alive(self):
            return self.h > 0

        def take_damage(self, attack):
            damage = max(0, attack - self.d)
            self.h -= damage
            if not self.is_alive:
                self.handle_death()
                return True

        def attack(self, other):
            return other.take_damage(self.a)

        def handle_death(self):
            self.g.removeObj(self.l)

    class Player(GameObject):

        direction_table = {
            "^": lambda self: (self.l[0], self.l[1] - 1),
            ">": lambda self: (self.l[0] + 1, self.l[1]),
            "v": lambda self: (self.l[0], self.l[1] + 1),
            "<": lambda self: (self.l[0] - 1, self.l[1]),
        }

        def __init__(self, game, s, l=None, b=None):
            super().__init__(game, 3, 1, 1, l)
            self.s = s
            self.b = b if b is not None else []
            self.exp = 0

        def __check_forward(self):
            new_loc = Player.direction_table[self.s](self)
            if self.g.is_within_bounds(new_loc):
                x, y = new_loc[0], new_loc[1]
                obj = self.g.field[y][x]
                return (new_loc, obj)
            else:
                return None

        def handle_death(self):
            self.g.player = None
            super().handle_death()

        def __find_item(self, item):
            for i in range(len(self.b)):
                if self.b[i] == item:
                    return self.b.pop(i)
            return None

        def __pickup_item(self, item):
            if item in "CKH":
                self.b.append(item)
            elif item == "X":
                self.a += 1
            else:
                self.d += 1

        def rotate(self, symb):
            self.s = symb
            x, y = self.l[0], self.l[1]
            self.g.field[y][x] = self.s

        def move(self):
            new_loc = self.__check_forward()
            if new_loc is None or new_loc[1] in "
            return False
            if new_loc[1] in "CKHSX":
                self.__pickup_item(new_loc[1])

            self.g.removeObj(self.l)
            self.l = new_loc[0]
            x, y = self.l[0], self.l[1]
            self.g.field[y][x] = self.s
            return True

        def attack(self):
            maybe_enemy = self.__check_forward()
            if maybe_enemy is None or maybe_enemy[1] not in "ED":
                return False

            loc, symb = maybe_enemy[0], maybe_enemy[1]
            if symb == "E":
                enemy = self.g.enemies[loc]
                if super().attack(enemy):
                    self.add_exp()
            else:
                super().attack(self.g.demonlord)
            return True

        def add_exp(self):
            self.exp += 1
            if self.exp == 3:
                self.a += 1
                self.exp = 0

        def use_item(self, item_s):
            item = self.__find_item(item_s)
            if item is None:
                return False

            if item == "H":
                if self.h < 3:
                    self.h = 3
                    return True
                else:
                    return False

            if item == "C":
                maybe_merch = self.__check_forward()
                if maybe_merch is None or maybe_merch[1] != "M":
                    return False

                merch_loc = maybe_merch[0]
                self.g.merchants[merch_loc].take_damage(1)
                return True

            if item == "K":
                maybe_door = self.__check_forward()
                if maybe_door is None or maybe_door[1] not in "-|":
                    return False

                door_loc = maybe_door[0]
                self.g.removeObj(door_loc)
                return True

    class Enemy(GameObject):
        def __init__(self, game, l=None):
            super().__init__(game, 1, 2, 0, l)

        def handle_death(self):
            del self.g.enemies[self.l]
            super().handle_death()

    class DemonLord(GameObject):
        def __init__(self, game, l=None):
            super().__init__(game, 10, 3, 0, l)

        def handle_death(self):
            self.g.demonlord = None
            super().handle_death()

    class Merchant(GameObject):
        def __init__(self, game, l=None):
            super().__init__(game, 3, 0, 0, l)

        def handle_death(self):
            del self.g.merchants[self.l]
            super().handle_death()

    class Game:
        def __init__(self, field):
            self.field = field
            self.player = None
            self.merchants = {}
            self.enemies = {}
            self.demonlord = None
            self.find_game_objects()

        def find_game_objects(self):
            for y in range(len(self.field)):
                for x in range(len(self.field[y])):
                    if self.field[y][x] == "M":
                        self.merchants[(x, y)] = Merchant(self, (x, y))
                    if self.field[y][x] == "E":
                        self.enemies[(x, y)] = Enemy(self, (x, y))
                    if self.field[y][x] == "D":
                        self.demonlord = DemonLord(self, (x, y))
                    if self.field[y][x] in "^><v":
                        self.player = Player(self, self.field[y][x], (x, y))

        def is_within_bounds(self, loc):
            return 0 <= loc[0] and loc[0] < len(self.field[0]) and 0 <= loc[1] and loc[1] < len(self.field)

        def check_enemies(self, loc):
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for d in directions:

                new_loc = (loc[0] + d[0], loc[1] + d[1])
                if self.is_within_bounds(new_loc):

                    if new_loc in self.enemies:
                        self.enemies[new_loc].attack(self.player)

                    elif self.demonlord and new_loc == self.demonlord.l:
                        self.demonlord.attack(self.player)

                if self.player is None:
                    return False
            return True

        def removeObj(self, loc):
            x, y = loc[0], loc[1]
            self.field[y][x] = " "

        def run_game(self, action_list):
            for action in action_list:
                prev_loc = self.player.l
                success = True
                if action in "^><v":
                    self.player.rotate(action)
                elif action == "A":
                    success = self.player.attack()
                elif action in "CKH":
                    success = self.player.use_item(action)
                else:
                    success = self.player.move()
                if not success:
                    return None

                is_alive = self.check_enemies(prev_loc)
                if not is_alive:
                    return None

            return (self.field, self.player.h, self.player.a, self.player.d, sorted(self.player.b))

    game = Game(game)
    return game.run_game(actions)
