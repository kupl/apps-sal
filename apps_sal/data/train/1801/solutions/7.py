class Memory:

    def __init__(self, width, height):
        self.__x = 0
        self.__y = 0
        self.width = width
        self.height = height
        self.mem = [[0] * width for _ in range(height)]

    def flip(self):
        self.mem[self.y][self.x] = (self.get() + 1) % 2

    def get(self):
        return self.mem[self.y][self.x]

    def to_string(self):
        return '\r\n'.join((''.join(map(str, row)) for row in self.mem))

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val % self.width

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val % self.height


def interpreter(code, iterations, width, height):
    op_ptr = 0
    mem = Memory(width, height)
    jumps = {}
    bracket = []
    for (i, op) in enumerate(code):
        if op == '[':
            bracket.append(i)
        elif op == ']':
            jumps[bracket[-1]] = i
            jumps[i] = bracket.pop()
    while iterations and op_ptr < len(code):
        op = code[op_ptr]
        if op in 'nesw*[]':
            iterations -= 1
        if op == 'n':
            mem.y -= 1
        elif op == 'e':
            mem.x += 1
        elif op == 's':
            mem.y += 1
        elif op == 'w':
            mem.x -= 1
        elif op == '*':
            mem.flip()
        elif op == '[' and mem.get() == 0:
            op_ptr = jumps[op_ptr]
        elif op == ']' and mem.get() != 0:
            op_ptr = jumps[op_ptr]
        op_ptr += 1
    return mem.to_string()
