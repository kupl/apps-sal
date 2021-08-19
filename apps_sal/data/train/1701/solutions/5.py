import operator
from functools import partialmethod, reduce


class Machine(object):
    def __init__(self, cpu):
        # Because Python ...
        cpu.read_reg = cpu.readReg
        cpu.write_reg = cpu.writeReg
        cpu.pop_stack = cpu.popStack
        cpu.push_stack = cpu.writeStack  # ... (and poor naming)
        self.cpu = cpu

    def execute(self, instruction):
        instr = instruction.replace(',', '').split()
        op, args = instr[0], instr[1:]
        op = '_{}'.format(op)

        getattr(self, op)(*args)

    def _push(self, values=None):
        for x in ensure_list(values):
            self.cpu.push_stack(self.value(x))

    def _pop(self, registers=None):
        for reg in ensure_list(registers):
            y = self.cpu.pop_stack()
            if reg:
                self.cpu.write_reg(reg, y)

    _pushr = partialmethod(_push, values=list('abcd'))
    _pushrr = partialmethod(_push, values=list('dcba'))
    _popr = partialmethod(_pop, registers=list('dcba'))
    _poprr = partialmethod(_pop, registers=list('abcd'))

    def _mov(self, a=None, b=None):
        self.cpu.write_reg(b, int(a))

    def value(self, var):
        try:
            return int(var)
        except ValueError:
            return self.cpu.read_reg(var)


def ensure_list(a):
    if not isinstance(a, list):
        a = [a]
    return a


def build_arithmetic_op(func):
    def f(machine, n=None, register='a'):
        result = func(machine.cpu.pop_stack() for x in range(machine.value(n)))
        machine.cpu.write_reg(register, int(result))
    return f


def push_a_then(func):
    def f(machine, *args, **kwargs):
        x = machine.cpu.read_reg('a')
        machine.cpu.push_stack(x)
        func(machine, *args, **kwargs)
    return f


_arithmetic = {
    '_add': sum,
    '_sub': lambda i: reduce(operator.sub, i),
    '_mul': lambda i: reduce(operator.mul, i),
    '_div': lambda i: reduce(operator.truediv, i),
    '_and': lambda i: reduce(operator.and_, i),
    '_or': lambda i: reduce(operator.or_, i),
    '_xor': lambda i: reduce(operator.xor, i),
}

for name, func in list(_arithmetic.items()):
    method = build_arithmetic_op(func)
    setattr(Machine, name, method)
    setattr(Machine, name + 'a', push_a_then(method))
