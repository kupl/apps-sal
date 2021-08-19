import sys
(mod, MOD) = (1000000007, 998244353)


def get_array():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().strip().split()))


def input():
    return sys.stdin.readline().strip()


T = int(input())
while T > 0:
    (a, b, n) = get_ints()
    n = n % 3
    if n == 0:
        print(a)
    elif n == 1:
        print(b)
    else:
        print(a ^ b)
    T -= 1
