class PlayerMovement:
    def __init__(self, x, y):
        self.position = Tile(x, y)
        self.direction = 8
        self.pressed = []
        self.movements = {8: (0, 1), 2: (0, -1), 6: (1, 0), 4: (-1, 0)}

    def update(self):
        newkey = False
        if any(Input.get_state(x) for x in (2, 4, 6, 8)):
            for x in (6, 4, 2, 8):
                if Input.get_state(x):
                    if not x in self.pressed:
                        self.pressed.append(x)
                        self.direction = x
                        newkey = True
                else:
                    if x in self.pressed:
                        if self.pressed[-1] == x:
                            newkey = True
                            if len(self.pressed) > 1:
                                self.direction = self.pressed[-2]
                        self.pressed.remove(x)
        else:
            self.pressed = []
            newkey = True
        if not newkey:
            self.position = Tile(self.position.x + self.movements[self.direction][0], self.position.y + self.movements[self.direction][1])
