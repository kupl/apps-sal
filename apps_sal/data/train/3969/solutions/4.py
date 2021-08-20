import math


def graceful_tipping(bill):
    x = math.ceil(bill + bill * 15 / 100)
    if x < 11:
        return x
    else:
        le = len(str(x)) - 2
        y = 5 * 10 ** le
        z = math.ceil(x / y)
        b = y * z - x
        x = x + b
    return x
