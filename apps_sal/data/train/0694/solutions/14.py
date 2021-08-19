from math import gcd
from functools import reduce


def lcm(denominators):
    return reduce(lambda a, b: a * b // gcd(a, b), denominators)


T = int(input())
for _ in range(T):
    n = int(input())
    text = input()
    list = [int(n) for n in text.split()]
    lcm_ans = lcm(list)
    print(n * 24 // lcm_ans)
