from collections import defaultdict
from ctypes import c_ubyte
from io import StringIO

class State:
    def __init__(self):
        self.selector = 0
        self.cells = defaultdict(c_ubyte)
        self.output = StringIO()

    @property
    def cell(self):
        return self.cells[self.selector]
        
    @cell.setter
    def cell(self, value):
        self.cells[self.selector] = value

    def execute(self, command):
        self.commands[command](self)

    def right(self):
        self.selector += 1

    def left(self):
        self.selector -= 1

    def inc(self):
        self.cell.value += 1

    def out(self):
        self.output.write(chr(self.cell.value))

    commands = defaultdict(lambda self: 0, {'>': right, '<': left, '+': inc, '*': out})
        

def interpreter(tape):
    s = State()
    for command in tape:
        s.execute(command)
    return s.output.getvalue()
