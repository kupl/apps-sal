ops = {'+': int.__add__, '-': int.__sub__, '*': int.__mul__, '/': int.__truediv__}


def calculator(x, y, op):
    if not (isinstance(x, int) and isinstance(y, int) and (op in ops)):
        return 'unknown value'
    return ops[op](x, y)
