def basic_op(o, a, b):
    return {'+': a + b, '-': a - b, '*': a * b, '/': a / b}.get(o)
