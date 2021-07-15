from operator import add, sub as subtract, mul as multiply

def calculate(n1, n2, o):
    value = globals()[o](int(n1, 2), int(n2, 2))
    return format(value, 'b')
