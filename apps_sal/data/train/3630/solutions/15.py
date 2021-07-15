from operator import add, sub, mul, truediv as div

def arithmetic(a, b, operator):
    return {'add': add, 'subtract': sub , 'multiply': mul, 'divide': div}[operator](a, b)
