from math import log


def compare_powers(n1, n2):
    val = n2[1] * log(n2[0]) - n1[1] * log(n1[0])
    return -1 if val < 0 else 1 if val > 0 else 0
