def calculate(n1, n2, o):
    ops = {'add': lambda a, b: a + b, 'subtract': lambda a, b: a - b, 'multiply': lambda a, b: a * b}
    n = ops[o](int(n1, 2), int(n2, 2))
    s = str(bin(n))
    return '-' + s[3:] if n < 0 else s[2:]
