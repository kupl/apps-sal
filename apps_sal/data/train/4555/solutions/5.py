import operator as op
from functools import reduce


def string_color(name):
    if name == '':
        return None
    lst = [ord(i) for i in name]
    a = sum(lst) % 256
    b = reduce(op.mul, lst) % 256
    c = (abs(lst[0] - sum(lst[1:]))) % 256
    a, b, c = format(a, 'x').upper().zfill(2), format(b, 'x').upper().zfill(2), format(c, 'x').upper().zfill(2)
    return a + b + c if not a == b == c else None
