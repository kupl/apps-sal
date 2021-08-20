import math


def add_binary(a, b):
    assert type(a) is int
    assert type(b) is int
    a = a + b
    exps = []
    while a != 0:
        b = int(math.floor(math.log(a, 2)))
        exps.append(b)
        if a == 1:
            break
        a = a % 2 ** b
    byte = ''.join((['0', '1'][x in exps] for x in range(exps[0], -1, -1)))
    return byte
