
import math


def facto(n):
    return math.factorial(n)


t = int(input())
while t:
    t = t - 1
    n = int(input())
    print(facto(n))
