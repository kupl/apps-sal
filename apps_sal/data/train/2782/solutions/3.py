OPS = {'+': lambda x, y: y + x, '-': lambda x, y: y - x, '*': lambda x, y: y * x, '/': lambda x, y: y / x}


def calc(expr):
    if not expr:
        return 0
    stack = []
    [stack.append(*map(OPS[sign], [stack.pop()], [stack.pop()])) if sign in OPS else stack.append(float(sign)) for sign in expr.split(' ')]
    return stack[-1]
