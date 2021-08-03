from numpy import sign


def reverse_number(n):
    return sign(n) * int(str(abs(n))[::-1])
