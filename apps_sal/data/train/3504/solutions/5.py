from math import floor


def power_mod(base, exponent, modulus):
    if (base < 0) or (exponent < 0) or (modulus < 1):
        return -1
    result = 1
    while exponent > 0:
        if (exponent % 2) == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent = floor(exponent / 2)
    return result
