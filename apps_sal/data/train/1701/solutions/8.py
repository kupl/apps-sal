from operator import add, sub, mul, floordiv, and_, or_, xor
from functools import reduce


class Machine(object):

    def __init__(self, cpu):
        self.cpu = cpu

    def execute(self, ins):
        (left, right) = ('abcd', 'dcba')
        cpu = self.cpu

        def value_of(x):
            return cpu.read_reg(x) if x in left else int(x)
        (i, *a) = ins.replace(',', '').split()
        if i.endswith('a'):
            cpu.write_stack(cpu.read_reg('a'))
            i = i[:-1]

        def seq(f):
            return cpu.write_reg(a[1] if len(a) > 1 else 'a', reduce(f, [cpu.pop_stack() for _ in range(value_of(a[0]))]))
        if i == 'push':
            cpu.write_stack(value_of(a[0]))
        elif i == 'pop':
            e = cpu.pop_stack()
            if len(a):
                cpu.write_reg(a[0], e)
        elif i == 'pushr':
            for c in left:
                self.execute('push ' + c)
        elif i == 'pushrr':
            for c in right:
                self.execute('push ' + c)
        elif i == 'popr':
            for c in right:
                self.execute('pop ' + c)
        elif i == 'poprr':
            for c in left:
                self.execute('pop ' + c)
        elif i == 'mov':
            cpu.write_reg(a[1], value_of(a[0]))
        elif i == 'add':
            seq(add)
        elif i == 'sub':
            seq(sub)
        elif i == 'mul':
            seq(mul)
        elif i == 'div':
            seq(floordiv)
        elif i == 'and':
            seq(and_)
        elif i == 'or':
            seq(or_)
        elif i == 'xor':
            seq(xor)
