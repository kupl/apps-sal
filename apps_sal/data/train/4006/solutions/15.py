def basic_op(o, v1, v2):
    return __import__('operator').__dict__[{'+': 'add', '-': 'sub', '*': 'mul', '/': 'truediv'}[o]](v1, v2)
