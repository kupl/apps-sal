import sys


def cal_power(a, n, m):
    if n == 0:
        return 1
    elif n == 1:
        return a % m
    elif not n % 2:
        return (cal_power(a, n // 2, m) % m) ** 2 % m
    else:
        return a % m * (cal_power(a, (n - 1) // 2, m) % m) ** 2 % m % m


def cal(b, n, m):
    if n == 0:
        return 0
    elif n == 1:
        return b % m
    elif not n % 2:
        return (1 + cal_power(b, n // 2, m)) % m * (cal(b, n // 2, m) % m) % m
    else:
        return ((1 + cal_power(b, (n + 1) // 2, m)) % m * (cal(b, (n - 1) // 2, m) % m) + cal_power(b, (n + 1) // 2, m) % m) % m


def solve(a, n, m):
    l = len(str(a))
    x = a % m
    q = 10 ** l % m
    return x * (1 + cal(q, n - 1, m)) % m


for _ in range(int(input())):
    (a, n, m) = [int(temp) for temp in input().split()]
    print(solve(a, n, m))
