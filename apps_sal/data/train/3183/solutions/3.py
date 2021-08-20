def interpreter(tape):
    infTick = Ticker()
    infTick.run(tape)
    return infTick.out


class Ticker:

    def error(x):
        return None
    doc = {'>': '_incr', '<': '_decr', '*': '_addA', '+': '_icrC', '-': '_dcrC', '/': '_skpZ', '\\': '_skpN', '&': '_error'}

    def __init__(self):
        self.cell = 0
        self.dat = [0] * 255
        self.out = ''
        self.skip = 0
        self.end = 0

    def skip(f):

        def wrap(cls):
            if not cls.skip:
                return f(cls)
            cls.skip = 0
        return wrap

    def run(self, com):
        while not self.end and len(self.out) != 256:
            [getattr(self, self.doc.get(k, 'error'))() for k in com]

    def _skpZ(self):
        if self.dat[self.cell] == 0:
            self.skip = 1

    def _skpN(self):
        if self.dat[self.cell] != 0:
            self.skip = 1

    @skip
    def _error(self):
        self.end = 1

    @skip
    def _addN(self):
        self.dat[self.cell] = ord(self.out[-1])

    @skip
    def _dcrC(self):
        self.dat[self.cell] -= 1

    @skip
    def _icrC(self):
        self.dat[self.cell] += 1

    @skip
    def _addA(self):
        self.out += chr(self.dat[self.cell] % 256)

    @skip
    def _incr(self):
        self.cell += 1

    @skip
    def _decr(self):
        self.cell -= 1
