def arithmetic(a, b, o):
    return __import__('operator').__dict__[o[:3].replace('div', 'truediv')](a, b)
