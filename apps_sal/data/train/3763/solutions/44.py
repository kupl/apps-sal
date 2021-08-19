import operator


def calculator(x, y, op):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    if op in ops and str(x).isdigit() and str(y).isdigit():
        return ops[op](x, y)
    else:
        return 'unknown value'
