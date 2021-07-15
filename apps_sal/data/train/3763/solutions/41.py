import operator as op

ops = {
    '+': op.add,
    '-': op.sub,
    '*': op.mul,
    '/': op.truediv,
}

def calculator(x, y, op):
    if op in ops and isinstance(x, int) and isinstance(y, int):
        return ops[op](x, y)
    return 'unknown value'
