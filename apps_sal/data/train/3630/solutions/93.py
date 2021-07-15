def arithmetic(a, b, op):
    return __import__('operator').__dict__['true' * (op[0] == 'd') + op[:3]](a, b)
