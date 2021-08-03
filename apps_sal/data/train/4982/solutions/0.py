class Game():

    def __init__(self, n):
        k = 2 * n + 1
        self.board = {frozenset(k * r + 1 + c + d for d in (0, n, n + 1, k))
                      for r in range(n) for c in range(n)}

    def play(self, lines):
        lines = set(lines)
        while 1:
            for cell in self.board:
                stick = cell - lines
                if len(stick) <= 1:
                    lines |= stick
                    self.board.remove(cell)
                    break
            else:
                break
        return sorted(lines)
