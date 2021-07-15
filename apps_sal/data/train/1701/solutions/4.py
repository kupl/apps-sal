from functools import partial, reduce
from operator import add, sub, mul, floordiv, and_, or_, xor
OPERATIONS = {'add': add, 'sub': sub, 'mul': mul, 'div': floordiv,
              'and': and_, 'or': or_, 'xor': xor}

class Machine(object):
    
    def __init__(self, cpu):
        self.cpu = cpu
    
    def read(self, reg):
        return self.cpu.readReg(reg)
    def mov(self, value, reg):
        self.cpu.writeReg(reg, int(value))
    
    def push(self, value):
        self.cpu.writeStack(int(value))
    def pop(self, reg=None):
        value = self.cpu.popStack()
        if reg: self.mov(value, reg)
        return value
    
    def pushr(self):
        for reg in 'abcd':
            self.push(self.read(reg))
    def pushrr(self):
        for reg in 'dcba':
            self.push(self.read(reg))
    def popr(self):
        for reg in 'dcba':
            self.pop(reg)
    def poprr(self):
        for reg in 'abcd':
            self.pop(reg)
    
    def _op_(self, op, n, reg='a'):
        values = (self.pop() for _ in range(n))
        self.mov(reduce(op, values), reg)
        
    def _opx_(self, op, src, n, reg='a'):
        self.push(self.read(src))
        self._op_(op, n, reg)
    
    def get(self, value):
        return int(value) if value.isdigit() else self.read(value)
    
    def execute(self, instr):
        cmd, _, args = instr.partition(' ')
        args = args.split(', ') if args else []
        if args and cmd != 'pop':
            args[0] = self.get(args[0])
        if cmd in OPERATIONS:
            self._op_(OPERATIONS[cmd], *args)
        elif cmd[:-1] in OPERATIONS:
            self._opx_(OPERATIONS[cmd[:-1]], cmd[-1], *args)
        else:
            getattr(self, cmd)(*args)
