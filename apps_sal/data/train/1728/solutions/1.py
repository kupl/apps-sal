class PlayerMovement:

    def __init__(self, x, y):
        self.position = Tile(x, y)
        self.direction = 8
        self.pressed = []

    def update(self):
        can_move = bool(self.pressed)
        for key in [6, 4, 2, 8]:
            pressed = Input.get_state(key)
            if not pressed and key in self.pressed:
                self.pressed.remove(key)
            elif pressed and key not in self.pressed:
                self.pressed.append(key)
        if self.pressed:
            if self.direction == self.pressed[-1] and can_move:
                self.move(self.direction)
            self.direction = self.pressed[-1]

    def move(self, direction):
        (dx, dy) = PlayerMovement.DIR_VECT[direction]
        self.position = Tile(self.position.x + dx, self.position.y + dy)


PlayerMovement.DIR_VECT = {8: (0, 1), 2: (0, -1), 4: (-1, 0), 6: (1, 0)}
