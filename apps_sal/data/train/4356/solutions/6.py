from functools import reduce
from operator import mul


def colorful(number):
    digits = [int(d) for d in str(number)]
    prods = []

    for size in range(1, len(digits) + 1):
        for start in range(len(digits) - size + 1):
            prods.append(reduce(mul, digits[start: start + size]))

    return len(prods) == len(set(prods))
