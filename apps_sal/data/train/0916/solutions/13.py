from sys import stdin
from math import ceil, gcd

# Input data
#stdin = open("input", "r")


def func():

    return

for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().split()))
    print(n * m // gcd(n, m))

