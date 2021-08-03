from functools import reduce
arop = {'add': lambda a, b: a + b, 'sub': lambda a, b: a - b, 'mul': lambda a, b: a * b, 'div': lambda a, b: a // b,
        'and': lambda a, b: a & b, 'or': lambda a, b: a | b, 'xor': lambda a, b: a ^ b}


class Machine(object):

    def __init__(self, cpu):
        self.cpu = cpu

    def rv(self, x):
        try:
            return int(x)
        except ValueError:
            return self.cpu.read_reg(x)

    def execute(self, instr):
        op, a, b = (instr.split(' ') + [None, None, None])[:3]
        if a:
            a = a.rstrip(',')
        if op in ('pushrr', 'poprr'):
            regs = 'dcba'
            op = op[:-1]
        else:
            regs = 'abcd'
        if op[-1:] == 'a':
            self.cpu.write_stack(self.cpu.read_reg('a'))
            op = op[:-1]
        if op == 'push':
            self.cpu.write_stack(self.rv(a))
        elif op in arop:
            self.cpu.write_reg(b if b else 'a', reduce(arop[op], (self.cpu.pop_stack() for _ in range(self.rv(a)))))
        elif op == 'mov':
            self.cpu.write_reg(b, self.rv(a))
        elif op == 'pop':
            if a:
                self.cpu.write_reg(a, self.cpu.pop_stack())
            else:
                self.cpu.pop_stack()
        elif op == 'pushr':
            for r in regs:
                self.cpu.write_stack(self.cpu.read_reg(r))
        elif op == 'popr':
            for r in regs[::-1]:
                self.cpu.write_reg(r, self.cpu.pop_stack())
