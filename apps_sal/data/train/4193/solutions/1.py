import math


def odd_dig_cubic(a, b):
    ret = []
    st = int(math.ceil(abs(a) ** (1.0 / 3.0)))
    en = int(abs(b) ** (1.0 / 3.0))
    if a < 0:
        st *= -1
    if b < 0:
        en *= -1
    for i in range(st, en):
        c = i ** 3
        if any((j in '02468' for j in str(c))):
            continue
        ret += [c]
    return ret
