from math import gcd  # Python versions 3.5 and above
# from fractions import gcd # Python versions below 3.5
from functools import reduce  # Python version 3.x


def lcm(denominators):
    return reduce(lambda a, b: a * b // gcd(a, b), denominators)


T = int(input())

for _ in range(T):

    n = int(input())

    text = input()
    list = [int(n) for n in text.split()]

    lcm_ans = lcm(list)
    print((n * 24) // lcm_ans)
