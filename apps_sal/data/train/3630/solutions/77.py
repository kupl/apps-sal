def arithmetic(a, b, o):
    return getattr(__import__('operator'), o == 'divide' and 'itruediv' or o[:3])(a, b)
