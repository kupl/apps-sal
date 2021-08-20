import math


def round_to_next5(n):
    return n if n % 5 == 0 else math.floor(n / 5) * 5 + 5
