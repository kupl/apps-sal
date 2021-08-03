from builtins import bin, oct, hex


def func(l):
    l = sum(l) // len(l)
    return [l, bin(l)[2:], oct(l)[2:], hex(l)[2:]]
