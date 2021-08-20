import math
from functools import reduce


def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


def GCD(list):
    return reduce(gcd, list)


for _ in range(eval(input())):
    n = eval(input())
    s = list(map(int, input().split()))
    ans = GCD(s)
    print(ans * n)
