def build_jump_table(code):
    jumps = {}
    stack = []
    for i, c in enumerate(code):
        if c == '[':
            stack.append(i)
        elif c == ']':
            j = stack.pop()
            jumps[i] = j
            jumps[j] = i
    return jumps

class Interpreter:
    def __init__(self, code, width, height):
        self.code = code
        self.jumps = build_jump_table(code)
        self.cells = [[0] * width for _ in range(height)]
        self.width = width
        self.height = height
        self.r = 0
        self.c = 0
        
    @property
    def value(self):
        return self.cells[self.r][self.c]

    @value.setter
    def value(self, val):
        self.cells[self.r][self.c] = val
        
    def run(self, iterations):
        pc = 0
        while pc < len(self.code) and iterations > 0:
            op = self.code[pc]
            if op == '*': self.value = 1 - self.value
            elif op == 'n': self.r = (self.r - 1) % self.height
            elif op == 's': self.r = (self.r + 1) % self.height
            elif op == 'w': self.c = (self.c - 1) % self.width
            elif op == 'e': self.c = (self.c + 1) % self.width
            elif op == '[' and self.value == 0: pc = self.jumps[pc]
            elif op == ']' and self.value == 1: pc = self.jumps[pc]
            pc += 1
            iterations -= op in '*nswe[]'
        return '\r\n'.join(''.join(map(str, row)) for row in self.cells)
    
def interpreter(code, iterations, width, height):
    ip = Interpreter(code, width, height)
    return ip.run(iterations)
