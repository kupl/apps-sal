class Game:

    def __init__(self, board):
        self.n = board

    def play(self, given):
        (n, make, given) = (self.n, [list(range(1, self.n + 1))], set(given))
        for i in range(n - 1):
            make.append([k + n + (n + 1) for k in make[-1]])
        (possible, i) = ([[i, i + n, i + n + 1, i + n + 1 + n] for i in sum(make, [])], 0)
        while i < len(possible):
            t = [k for k in possible[i] if k not in given]
            if len(t) == 1:
                given.add(t[0])
                i = -1
            i += 1
        return sorted(given)
