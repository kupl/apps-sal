import random


class Interpretor(object):
    """
    0-9 Push this number onto the stack.
    " Start string mode: push each character's ASCII value all the way up to the next ".
    """

    def __init__(self, lines):
        self.code = [list(line) for line in lines.split('\n')]
        def push(a): return self.stack.append(a)

        self.no_parameter_ops = {
            '>': lambda: self.change_dir(1, 0),
            '<': lambda: self.change_dir(-1, 0),
            '^': lambda: self.change_dir(0, -1),
            'v': lambda: self.change_dir(0, 1),
            '?': lambda: self.change_dir(*random.choice([[1, 0], [-1, 0], [0, -1], [0, 1]])), '
            ' ': lambda: None,
            '@': self.stop,
            '"': self.toggle_string
        }

        self.one_parameter_ops = {
            '!': lambda a: push(1 if a == 0 else 0),
            '_': lambda a: self.change_dir(1, 0) if a == 0 else self.change_dir(-1, 0),
            '|': lambda a: self.change_dir(0, 1) if a == 0 else self.change_dir(0, -1),
            ':': lambda a: push(0) if a is None else [push(a), push(a)],
            '$': lambda a: None,
            '.': lambda a: self.output.append(a),
            ',': lambda a: self.output.append(chr(a))
        }

        self.two_parameter_ops = {
            '+': lambda a, b: push(b + a),
            '-': lambda a, b: push(b - a),
            '*': lambda a, b: push(a * b),
            '/': lambda a, b: push(0 if a == 0 else b / a),
            '%': lambda a, b: push(0 if a == 0 else b % a),
            '`': lambda a, b: push(1 if b > a else 0),
            '\\': lambda a, b: [push(a), push(0)] if b is None else [push(a), push(b)],
            'g': lambda y, x: push(ord(self.code[y][x]))
        }

        self.tri_parameter_ops = {
            'p': self.put
        }

    def put(self, y, x, v): self.code[y][x] = chr(v)
    def stop(self): self.running = False
    def change_dir(self, nx, ny): self.dx, self.dy = nx, ny
    def toggle_string(self): self.string = not self.string

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def interpret(self):
        self.stack = []
        self.output = []
        self.x, self.y = 0, 0
        self.dx, self.dy = 1, 0
        self.running = True
        self.string = False

        def pop(): return self.stack.pop() if self.stack else None

        while self.running:
            self.y = self.y % len(self.code)
            self.x = self.x % len(self.code[self.y])
            token = self.code[self.y][self.x]

            if self.string and token != "\"":
                self.stack.append(ord(token))
            elif token in self.no_parameter_ops:
                self.no_parameter_ops[token]()
            elif token in self.one_parameter_ops:
                self.one_parameter_ops[token](pop())
            elif token in self.two_parameter_ops:
                self.two_parameter_ops[token](pop(), pop())
            elif token in self.tri_parameter_ops:
                self.tri_parameter_ops[token](pop(), pop(), pop())
            elif token in "0123456789":
                self.stack.append(int(token))

            self.move()
        return ''.join(str(x) for x in self.output)


def interpret(code):
    interpretor = Interpretor(code)
    return interpretor.interpret()
