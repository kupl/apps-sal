from sys import stdin
from math import ceil, gcd


def func():
    return


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    s = 0
    for ele in arr:
        if ele % 2 == 0:
            s += ele
    print(s)
