import random

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


class Befunge93Instance:
    def __init__(self, code, step_limit=9999):
        self.code = [[i for i in line] for line in code.split('\n')]
        for line in code.split('\n'):
            print(line)
        self.head = [0, 0]
        self.stack = []
        self.direction = directions[0]
        self.output = ''
        self.string_mode = False
        self.steps = 0
        self.step_limit = step_limit

    def get_instr(self):
        try:
            return self.code[self.head[0]][self.head[1]]
        except IndexError:
            print(('head out of range: {}'.format(self.head)))
            return 0

    def set_direction(self, direction_index):
        self.direction = directions[direction_index]

    def advance_head(self):
        self.head[0] += self.direction[0]
        self.head[1] += self.direction[1]

    def pop_stack(self) -> int:
        try:
            return self.stack.pop()
        except IndexError:
            return 0

    def push_stack(self, item):
        try:
            self.stack.append(int(item))
        except ValueError:
            self.stack.append(int(ord(item)))

    def operation(self, op):
        try:
            a = self.pop_stack()
            b = self.pop_stack()
            self.stack.append(op(a, b))
        except ZeroDivisionError:
            self.stack.append(0)

    def print_status(self):
        print()
        print(('{} output({})'.format(self.steps, self.output)))
        print((self.stack))
        print(('head {} dir {} instr {}'.format(self.head, self.direction, self.get_instr())))

    def exec_instr(self) -> bool:
        self.steps += 1

        if self.steps > self.step_limit:
            return False

        instr = self.get_instr()

        if self.string_mode:
            if instr == '\"':
                self.string_mode = False
            else:
                self.push_stack(instr)
            self.advance_head()
            return True

        if instr in '0123456789':
            self.stack.append(int(instr))
        elif instr == '+':
            self.operation(lambda a, b: a + b)
        elif instr == '-':
            self.operation(lambda a, b: b - a)
        elif instr == '*':
            self.operation(lambda a, b: a * b)
        elif instr == '/':
            self.operation(lambda a, b: b // a)
        elif instr == '%':
            self.operation(lambda a, b: b % a)
        elif instr == '!':
            self.push_stack(not self.pop_stack())
        elif instr == '`':
            self.operation(lambda a, b: int(b > a))
        elif instr in '><v^':
            self.set_direction('><v^'.index(instr))
        elif instr == '?':
            self.set_direction(random.randint(0, 3))
        elif instr == '_':
            if self.pop_stack() == 0:
                self.set_direction(0)
            else:
                self.set_direction(1)
        elif instr == '|':
            if self.pop_stack() == 0:
                self.set_direction(2)
            else:
                self.set_direction(3)
        elif instr == '\"':
            self.string_mode = True
        elif instr == ':':
            try:
                self.stack.append(self.stack[-1])
            except IndexError:
                self.stack.append(0)
        elif instr == '\\':
            try:
                self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
            except IndexError:
                self.stack.append(0)
        elif instr == '$':
            self.pop_stack()
        elif instr == '.':
            self.output += str(self.pop_stack())
        elif instr == ',':
            self.output += chr(self.pop_stack())
        elif instr == '
        self.advance_head()
        elif instr == 'p':
            x = self.pop_stack()
            y = self.pop_stack()
            value = self.pop_stack()
            self.code[x][y] = chr(value)
        elif instr == 'g':
            x = self.pop_stack()
            y = self.pop_stack()
            self.push_stack(ord(self.code[x][y]))
        elif instr == '@':
            return False

        self.advance_head()
        return True

    def run(self):
        while self.exec_instr():
            pass


def interpret(code):
    interpreter = Befunge93Instance(code)
    interpreter.run()
    return interpreter.output
