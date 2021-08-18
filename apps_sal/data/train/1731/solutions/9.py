import inspect
import random


def interpret(s):
    return Befunge93(s.splitlines()).run()


class Befunge93:

    instructions = {}

    def __init__(self, plane):
        self.plane = [list(row) for row in plane]
        self.stack = []
        self.direction = [0, 1]
        self.row, self.col = 0, 0
        self.running = True
        self.output = []
        self.number = 0

    def forward(self):
        if self.number:
            self.row += self.direction[0]
            self.col += self.direction[1]
        self.number += 1
        return self.plane[self.row][self.col]

    def string_literal(self):
        self.stack.extend(ord(ch) for ch in iter(self.forward, '"'))

    def run(self):
        while self.running:
            self.instructions[self.forward()](self)
        return ''.join(self.output)


def pop_push_on(ch):
    def deco(f):
        nargs = len(inspect.getargspec(f).args)

        def wrapper(self):
            self.stack.append(f(*[self.stack.pop() for i in range(nargs)]))
        Befunge93.instructions[ch] = wrapper
        return wrapper
    return deco


def on(ch): return lambda f: Befunge93.instructions.__setitem__(ch, f)


pop_push_on('+')(lambda a, b: a + b)
pop_push_on('-')(lambda a, b: b - a)
pop_push_on('*')(lambda a, b: a * b)
pop_push_on('/')(lambda a, b: b // a if a else 0)
pop_push_on('%')(lambda a, b: b % a if a else 0)
pop_push_on('!')(lambda a: 0 if a else 1)
pop_push_on('`')(lambda a, b: 1 if b > a else 0)
on('>')(lambda self: self.direction.__setitem__(slice(None), [0, +1]))
on('<')(lambda self: self.direction.__setitem__(slice(None), [0, -1]))
on('^')(lambda self: self.direction.__setitem__(slice(None), [-1, 0]))
on('v')(lambda self: self.direction.__setitem__(slice(None), [+1, 0]))
on('?')(lambda self: self.direction.__setitem__(slice(None), random.choice([[0, +1], [0, -1], [-1, 0], [+1, 0]])))
on('_')(lambda self: self.direction.__setitem__(slice(None), [0, +1] if self.stack.pop() == 0 else [0, -1]))
on('|')(lambda self: self.direction.__setitem__(slice(None), [+1, 0] if self.stack.pop() == 0 else [-1, 0]))
on('|')(lambda self: self.direction.__setitem__(slice(None), [+1, 0] if self.stack.pop() == 0 else [-1, 0]))
on(':')(lambda self: self.stack.append(self.stack[-1] if self.stack else 0))
on('\\')(lambda self: self.stack.append(self.stack.pop(-2) if len(self.stack) >= 2 else 0))
on(' ')(lambda self: 0)
on('@')(lambda self: setattr(self, 'running', False))
on('$')(lambda self: self.stack.pop())
on('.')(lambda self: self.output.append(str(self.stack.pop())))
on(',')(lambda self: self.output.append(chr(self.stack.pop())))
on('
on('"')(lambda self: self.string_literal())
on('p')(lambda self: self.plane[self.stack.pop()].__setitem__(self.stack.pop(), chr(self.stack.pop())))
on('g')(lambda self: self.stack.append(ord(self.plane[self.stack.pop()][self.stack.pop()])))
for ch in '0123456789':
    on(ch)(lambda self, ch=int(ch): self.stack.append(ch))
