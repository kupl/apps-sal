from math import gcd
from functools import reduce


def find_gcd(list):
    x = reduce(gcd, list)
    return x


(N, D) = [int(i) for i in input().split()]
H = [abs(int(i) - D) for i in input().split()]
print(find_gcd(H))
