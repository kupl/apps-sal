class PlayerMovement:

    def __init__(self, x, y):
        self.position = Tile(x, y)
        self.direction = 8
        self.stack = []
        self.moves = {8: [0, 1], 2: [0, -1], 4: [-1, 0], 6: [1, 0]}

    def update(self):
        self.stack = list(filter(lambda x: Input.get_state(x), self.stack))

        firsttimer = False
        for i in [6, 4, 2, 8]:
            if not i in self.stack and Input.get_state(i):
                firsttimer = True
                self.stack.append(i)

        if not self.stack:
            return

        winner = self.stack[-1]

        if winner != self.direction or firsttimer:
            self.direction = winner
        else:
            move = self.moves[self.direction]
            self.position = Tile(self.position.x + move[0], self.position.y + move[1])
