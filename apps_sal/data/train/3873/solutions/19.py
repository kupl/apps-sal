from operator import mul
from functools import reduce


def product_sans_n(numbers):
    check = reduce(mul, numbers)
    out = []

    if not check:
        for i in range(len(numbers)):
            c = reduce(mul, numbers[:i] + numbers[i + 1:])
            out.append(c)

    else:
        for x in numbers:
            out.append(check // x)

    return out
