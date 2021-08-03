from functools import reduce


class Machine(object):

    def __init__(self, cpu):
        self.cpu = cpu

    def execute(self, instr):
        i = instr
        if i[0] == 'p':
            def doa(a):
                for k, l in a:
                    self.cpu.write_stack(l)

            def dob(a):
                for k in a:
                    self.cpu.write_reg(k, self.cpu.pop_stack())
            inst = i.split()
            if inst[0] == 'push':
                self.cpu.write_stack(self.cpu.read_reg(inst[1]) if inst[1].isalpha() else int(inst[1]))
            elif inst[0] == 'pop':
                if len(inst) == 1:
                    self.cpu.pop_stack()
                else:
                    self.cpu.write_reg(inst[1], self.cpu.pop_stack())
            elif inst[0] == 'pushr':
                doa(self.cpu.registers.items())
            elif inst[0] == 'pushrr':
                doa(reversed(list(self.cpu.registers.items())))
            elif inst[0] == 'popr':
                dob(['d', 'c', 'b', 'a'])
            elif inst[0] == 'poprr':
                dob(['a', 'b', 'c', 'd'])
        elif i.startswith('mov'):
            inst = i.replace(",", '').split()
            self.cpu.write_reg(inst[2], self.cpu.read_reg(inst[1]) if inst[1].isalpha() else int(inst[1]))
        else:
            def do(inst, op, a, b, l):
                reg, val = 'a' if l == 2 else inst[2], self.cpu.read_reg(inst[1]) if inst[1].isalpha() else int(inst[1])
                s = self.cpu.read_reg('a') if inst[0][-1] == 'a' else (self.cpu.pop_stack() if a else (0 if op == '+' else 1))
                s = reduce(lambda x, y: eval('x {} y'.format(op)), [s] + [self.cpu.stack.pop() for _ in range(val - b)])
                self.cpu.write_reg(reg, s)
            inst = i.replace(',', '').split()
            l = len(inst)
            if inst[0].startswith('add'):
                do(inst, '+', 0, inst[0][-1] == 'a', l)
            elif inst[0].startswith('sub'):
                do(inst, '-', 1, 1, l)
            elif inst[0].startswith('mul'):
                do(inst, '*', 0, inst[0][-1] == 'a', l)
            elif inst[0].startswith('div'):
                do(inst, '//', 1, 1, l)
            elif inst[0].startswith('and'):
                do(inst, '&', 1, 1, l)
            elif inst[0].startswith('or'):
                do(inst, '|', 0, inst[0][-1] == 'a', l)
            elif inst[0].startswith('xor'):
                do(inst, '^', 0, inst[0][-1] == 'a', l)
