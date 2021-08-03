from collections import defaultdict


def interpreter(tape):
    memory = Memory()
    memory.read(tape)
    return memory.output


class Memory(object):
    def __init__(self):
        self.cells, self.cur, self.output = defaultdict(int), 0, ""
        self.command = {">": self.nxt, "<": self.prv, "+": self.inc, "*": self.write}

    def read(self, tape):
        [self.command[c]() for c in tape if c in self.command]

    def prv(self):
        self.cur -= 1

    def nxt(self):
        self.cur += 1

    def inc(self):
        self.cells[self.cur] += 1

    def write(self):
        self.output = f"{self.output}{chr(self.cells[self.cur] % 256)}"
