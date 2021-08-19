from sys import stdin
from math import ceil, gcd


def func():
    return


for _ in range(int(stdin.readline())):
    (n, m) = list(map(int, stdin.readline().split()))
    print(n * m // gcd(n, m))
