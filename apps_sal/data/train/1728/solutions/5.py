class PlayerMovement:

    PREC = [8, 2, 4, 6]
    I_KEYS = {8: 0, 2: 1, 4: 2, 6: 3}
    MOVES = {8: (0, 1), 2: (0, -1), 4: (-1, 0), 6: (1, 0)}

    def __init__(self, x, y):
        self.position = Tile(x, y)
        self.direction = 8
        self.pressed = [0, 0, 0, 0]
        self.stack = []

    def update(self):
        state = [Input.get_state(d) for d in self.PREC]

        newPressed = [d for i, d in enumerate(self.PREC) if not self.pressed[i] and state[i]]
        notReleased = next((d for d in self.stack[::-1] if self.pressed[self.I_KEYS[d]] and state[self.I_KEYS[d]]), None)
        releasedLst = [d for i, d in enumerate(self.PREC) if self.pressed[i] and not state[i]]

        if newPressed:
            self.direction = newPressed[0]
            for t in newPressed[::-1]:
                self.stack.append(t)

        elif self.direction in releasedLst:
            self.direction = notReleased or self.direction

        elif notReleased:
            self.position = Tile(*(z + dz for z, dz in zip([self.position.x, self.position.y], self.MOVES[notReleased])))

        self.pressed = state
        for t in releasedLst:
            self.stack.remove(t)
