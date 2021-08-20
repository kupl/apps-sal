def get_generation(cells, gen):
    ng = Life(cells)
    return Life.process(ng, gen)


class Life:
    neighbor = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x or y]

    def __init__(self, cells):
        self.cells = [e[:] for e in cells]
        self._forLife = lambda x, y: int(self._express(x, y) in (2, 3))
        self._forDead = lambda x, y: int(self._express(x, y) == 3)

    @property
    def _lenY(self):
        return len(self.cells[0])

    @property
    def core(self):
        return {(x, y): c for (x, e) in enumerate(self.cells) for (y, c) in enumerate(e)}

    def _express(self, xc, yc):
        core = self.core
        return sum((self.cells[x + xc][y + yc] for (x, y) in self.neighbor if core.get((x + xc, y + yc)) != None))

    @classmethod
    def process(cls, self, gen):
        for _ in range(gen):
            cls._add_field(self)
            nextG = [e[:] for e in self.cells]
            for ((x, y), c) in self.core.items():
                nextG[x][y] = {0: self._forDead, 1: self._forLife}.get(c)(x, y)
            self.cells = cls._del_field(nextG)
        return self.cells

    @classmethod
    def _add_field(cls, self):
        for _ in range(4):
            self.cells = [list(e) for e in zip(*self.cells[::-1])]
            if any(self.cells[0]):
                self.cells.insert(0, [0] * self._lenY)

    @staticmethod
    def _del_field(field, cut=4):
        for _ in range(4):
            field = [list(e) for e in zip(*field[::-1])]
            while not any(field[0]):
                field.pop(0)
        return field
