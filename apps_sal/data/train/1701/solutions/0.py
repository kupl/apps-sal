from operator import add, sub, mul, floordiv as div, and_, or_, xor
OP = {'add': add, 'sub': sub, 'mul': mul, 'div': div, 'and': and_, 'or': or_, 'xor': xor}


class Machine(object):

    def __init__(self, cpu):
        self.cpu = cpu

    def execute(self, instruction):
        (cmd, a, b) = (instruction.replace(',', ' ') + ' 0 0').split()[:3]
        v = self.cpu.read_reg(a) if a in 'abcd' else int(a)
        if cmd == 'mov':
            self.cpu.write_reg(b, v)
        elif cmd == 'pop':
            self.cpu.write_reg(a, self.cpu.pop_stack()) if a in 'abcd' else self.cpu.pop_stack()
        elif cmd == 'push':
            self.cpu.write_stack(v)
        elif cmd in ['pushr', 'pushrr']:
            for r in 'abcd' if cmd == 'pushr' else 'dcba':
                self.cpu.write_stack(self.cpu.read_reg(r))
        elif cmd in ['popr', 'poprr']:
            for r in 'abcd' if cmd == 'poprr' else 'dcba':
                self.cpu.write_reg(r, self.cpu.pop_stack())
        else:
            r = self.cpu.pop_stack() if cmd[-1] != 'a' else self.cpu.read_reg('a')
            for _ in range(v - 1):
                r = OP[cmd if cmd[-1] != 'a' else cmd[:-1]](r, self.cpu.pop_stack())
            self.cpu.write_reg(b if b in 'abcd' else 'a', r)
