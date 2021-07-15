def func_or(a, b):
    return bool(a if a else b)

def func_xor(a, b):
    return bool(not b if a else b)
