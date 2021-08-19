def interpreter(tape):
    test = Ticker(tape)
    test.run()
    return test.out


class Ticker:

    def error(x):
        return None
    doc = {'>': '_incr', '<': '_decr', '*': '_addA', '+': '_icrC', '-': '_dcrC', '/': '_skpZ', '\\': '_skpN', '&': '_error'}

    def __init__(self, tape):
        self.com = tape
        self.cell = 0
        self.dat = [0] * 255
        self.out = ''
        self.skip = 0
        self.end = 0

    def skip(f):

        def wrap(cond):
            if not cond.skip:
                return f(cond)
            cond.skip = 0
        return wrap

    def run(self):
        while not self.end and len(self.out) != 256:
            [getattr(self, self.doc.get(k, 'error'))() for k in self.com]

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
