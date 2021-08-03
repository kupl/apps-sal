from enum import IntEnum


class PlayerMovement:

    class Dir(IntEnum):
        UP = 4
        DOWN = 3
        LEFT = 2
        RIGHT = 1

        @classmethod
        def get_dir(cls, key):
            map = {8: cls.UP, 2: cls.DOWN, 4: cls.LEFT, 6: cls.RIGHT}
            return map[key]

        @classmethod
        def get_key(cls, dir):
            map = {cls.UP: 8, cls.DOWN: 2, cls.LEFT: 4, cls.RIGHT: 6}
            return map[dir]

        @classmethod
        def get_move(cls, dir):
            map = {cls.UP: (0, 1), cls.DOWN: (0, -1), cls.LEFT: (-1, 0), cls.RIGHT: (1, 0)}
            return map[dir]

    def __init__(self, x, y):
        self.position = Tile(x, y)
        self.direction = 8
        self.directions = []

    def update_directions(self):
        pressed = [self.Dir.get_dir(x) for x in (8, 2, 4, 6) if Input.get_state(x) == True]
        self.directions = [x for x in self.directions if x in pressed]
        pressed.sort()
        for x in pressed:
            if x not in self.directions:
                self.directions.append(x)

    def update(self):
        directions_before = self.directions
        self.update_directions()
        if len(self.directions) == 0:
            pass
        elif self.directions[-1] != self.Dir.get_dir(self.direction) \
                or self.directions[-1] not in directions_before:
            self.direction = self.Dir.get_key(self.directions[-1])
        else:
            move = self.Dir.get_move(self.directions[-1])
            self.position = Tile(self.position.x + move[0], self.position.y + move[1])
