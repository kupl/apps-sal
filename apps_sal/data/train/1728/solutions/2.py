class PlayerMovement:

    KEYS = 6, 4, 2, 8
    DIRS = dict(list(zip(KEYS, ((1, 0),
                                (-1, 0),
                                (0, -1),
                                (0, 1)))))

    def __init__(self, x, y):
        self.position = Tile(x, y)
        self.direction = 8
        self.previous = {i: False for i in self.KEYS}
        self.keystack = [0]

    def update(self):
        current = dict(list(Input.STATES.items()))
        if (current != self.previous):
            change = {i: current[i] - self.previous[i]
                      for i in self.KEYS}
            for key in self.KEYS:
                if change[key] > 0:
                    self.keystack.append(key)
                elif change[key] < 0:
                    self.keystack.remove(key)
        if (self.keystack[-1] == self.direction
                and sum(self.previous.values())):
            dx, dy = self.DIRS[self.direction]
            self.position = Tile(self.position.x + dx,
                                 self.position.y + dy)
        else:
            self.direction = self.keystack[-1] or self.direction
        self.previous = current
