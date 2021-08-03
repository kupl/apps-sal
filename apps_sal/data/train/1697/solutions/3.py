from itertools import groupby, product


class Nonogram:
    def __init__(self, clues):
        self.clues = clues

    def solve(self):
        for p in product(
            *[[p for p in product(range(2), repeat=5)
               if sum(p) == sum(t) and tuple(len(list(g)) for k, g in groupby(p) if k) == t]
              for t in self.clues[1]]
        ):
            if all(tuple(len(list(g)) for k, g in groupby(p) if k) == t
                   for p, t in zip([v for v in zip(*p)], self.clues[0])):
                return p
