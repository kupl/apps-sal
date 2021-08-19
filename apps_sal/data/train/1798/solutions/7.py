def get_generation(cells, gen):
    ng = Life(cells)
    return ng.process(gen)


class Life:

    def __init__(self, cells):
        self.cells = [e[:] for e in cells]
        self.neighbor = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x or y]
        self._forLife = lambda x, y: int(self._express(x, y) in (2, 3))
        self._forDead = lambda x, y: int(self._express(x, y) == 3)

    @property
    def _lenX(self):
        return len(self.cells)

    @property
    def _lenY(self):
        return len(self.cells[0])

    @property
    def core(self):
        return {(x, y): c for (x, e) in enumerate(self.cells) for (y, c) in enumerate(e)}

    def _express(self, xc, yc):
        core = self.core
        return sum((self.cells[x + xc][y + yc] for (x, y) in self.neighbor if core.get((x + xc, y + yc)) != None))

    def process(self, gen):
        for _ in range(gen):
            self._add_field()
            nextG = [e[:] for e in self.cells]
            for ((x, y), c) in list(self.core.items()):
                nextG[x][y] = {0: self._forDead, 1: self._forLife}.get(c)(x, y)
            self.cells = self._del_field(nextG)
        return self.cells

    def _add_field(self):
        for (i, (s, e)) in enumerate([(0, self._lenY + 1)] * self._lenX):
            self.cells[i].insert(s, 0)
            self.cells[i].insert(e, 0)
        for _ in (s, e + 1):
            self.cells.insert(_, [0] * self._lenY)

    def _del_field(self, field, cut=4):
        for _ in range(4):
            field = [list(e) for e in zip(*field[::-1])]
            while not any(field[0]):
                field.pop(0)
        return field
