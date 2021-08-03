class Game():
    def __init__(self, board):
        self.board = board

    def play(self, lines):
        self.lines = set(lines)
        change = True
        while change:
            change = False
            for row in range(self.board):
                for col in range(self.board):
                    offset = row * (2 * self.board + 1)
                    top = offset + col + 1
                    left = top + self.board
                    right = left + 1
                    bottom = right + self.board
                    cell = [top, left, right, bottom]
                    sides = 0
                    for side in cell:
                        if side in self.lines:
                            sides += 1
                    if sides == 3:
                        self.lines = self.lines.union(set(cell))
                        change = True
        return sorted(list(self.lines))
