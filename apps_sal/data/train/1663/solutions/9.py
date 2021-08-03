# Python 3.8 when
# https://stackoverflow.com/a/53983683
def isqrt(n):
    if n > 0:
        x = 1 << (n.bit_length() + 1 >> 1)
        while True:
            y = (x + n // x) >> 1
            if y >= x:
                return x
            x = y
    elif n == 0:
        return 0
    else:
        raise ValueError("square root not defined for negative numbers")


def count_divisors(n):
    s = isqrt(n)
    return 2 * sum(n // i for i in range(1, s + 1)) - s * s
