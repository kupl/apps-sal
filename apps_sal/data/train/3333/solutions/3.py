def func_or(*a):
    return any(a)

def func_xor(*a):
    return any(a) and not all(a)
