from math import floor
Q = int(input())
E = 10**(-10)


def f(x):
    if min(abs(int(x) - x), abs(int(x) + 1 - x)) < E:
        return int(x - 1)
    else:
        return int(x)


for i in range(Q):
    a, b = list(map(int, input().split()))
    n = a * b
    if f(n**(1 / 2)) < a and f(n**(1 / 2)) < b:
        if f(n**(1 / 2)) * (f(n**(1 / 2)) + 1) < n:
            print((2 * f(n**(1 / 2))))
        else:
            print((2 * f(n**(1 / 2)) - 1))
    else:
        if f(n**(1 / 2)) * (f(n**(1 / 2)) + 1) < n:
            print((2 * f(n**(1 / 2)) - 1))
        else:
            print((2 * f(n**(1 / 2)) - 2))
