def func_or(a, b):
    if a:
        return True
    else:
        return not not b


def func_xor(a, b):
    if a:
        return not b
    else:
        return not not b
