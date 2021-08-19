from operator import add, sub, mul, truediv as div
OPS = dict(list(zip('+-*/', (add, sub, mul, div))))
foo = lambda *args: 'unknown value'


def calculator(x, y, op):
    return OPS.get(op, foo)(x, y) if all((isinstance(i, (int, float)) for i in (x, y))) else foo()
