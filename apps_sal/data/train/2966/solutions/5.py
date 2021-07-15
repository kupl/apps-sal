from re import findall

def calculate(s):
    op1, op2 = map(int, findall('(\d+)', s))
    return op1 + op2 if 'gains' in s else op1 - op2
