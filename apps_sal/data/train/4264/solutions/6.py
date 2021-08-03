from math import log2


def operation(a, b):
    if a in (0, b):
        return 0
    c = 0
    while a != b:
        if a % 2 and a > 1:
            a = (a - 1) // 2
        elif a < b and log2(a).is_integer():
            a *= 2
        elif a > b or not log2(a).is_integer():
            a //= 2
        c += 1
    return c
