from itertools import accumulate
from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y) if x else y


candies_to_buy = list(accumulate(range(2000), lcm)).__getitem__
