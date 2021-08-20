from math import gcd
from functools import reduce


def lcm(denominators):
    return reduce(lambda a, b: a * b // gcd(a, b), denominators)


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    res = lcm(arr)
    hrs = 24 * n
    print(hrs // res)
