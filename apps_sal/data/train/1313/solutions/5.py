from functools import reduce
from math import gcd


def divisor(n):
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n


for _ in range(int(input())):
    n = int(input())
    ls = [int(X) for X in input().split()]
    gc = reduce(gcd, ls)
    if gc == 1:
        print(-1)
    elif gc % 2 == 0:
        print(2)
    else:
        print(divisor(gc))
