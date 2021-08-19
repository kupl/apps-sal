import math


def nth_perm(n, d):
    digits = [str(i) for i in range(d)]
    out = ''
    for i in range(1, d):
        cycles = math.ceil(n / math.factorial(d - i))
        out += digits.pop(cycles % (d - i + 1) - 1)
    return out + digits.pop()
