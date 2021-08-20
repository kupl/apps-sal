class Game:

    def __init__(self, n):
        k = 2 * n + 1
        self.board = [{k * r + 1 + c, k * (r + 1) + 1 + c, k * r + n + 1 + c, k * r + n + 2 + c} for r in range(n) for c in range(n)]

    def play(self, lines):
        (L, last) = (set(lines), None)
        while self.board != last:
            last = self.board[:]
            for k in [s for s in self.board if len(L & s) == 3]:
                L |= k
                self.board.remove(k)
        return sorted(list(L))
