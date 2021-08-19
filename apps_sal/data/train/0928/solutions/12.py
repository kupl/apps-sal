from sys import stdin
from math import ceil, gcd


def func():
    return


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    ans = 0
    i = 1
    while i * i <= n:
        if i * i % 3 != 0:
            ans += 1
        i += 1
    print(ans)
