import math


def get_positions(n):
    return (n % 3, math.floor((n / 3) % 3), math.floor((n / 9) % 3))
