def interpreter(tape):
    test = Ticker(tape)
    return test.out


class Ticker:

    def error(x):
        return None
    doc = {'>': '_incr', '<': '_decr', '*': '_addA', '+': '_icrC', '-': '_dcrC', '/': '_set', '!': '_addN'}

    def __init__(self, tape):
        self.dat = [0] * 256
        self.ind = 0
        self.out = ''
        self.run = [getattr(self, self.doc.get(k, 'error'))() for k in tape]

    def _set(self, dflt=0):
        self.dat[self.ind] = 0

    def _addN(self):
        self.dat[self.ind] = ord(self.out[-1])

    def _dcrC(self):
        self.dat[self.ind] -= 1

    def _icrC(self):
        self.dat[self.ind] += 1

    def _addA(self):
        self.out += chr(self.dat[self.ind] % 256)

    def _incr(self):
        self.ind += 1

    def _decr(self):
        self.ind -= 1
