from math import log10, floor


def digits(n: int) -> int:
    return floor(log10(n) + 1) if n else 0
