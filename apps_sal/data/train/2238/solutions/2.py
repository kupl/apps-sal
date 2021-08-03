from math import log2


def solve(a, b):
    if a == b:
        return a
    x = int(log2(b))
    if 2**x <= a:
        return solve(a - 2**x, b - 2**x) + 2**x

    if 2**(x + 1) - 1 <= b:
        return 2**(x + 1) - 1

    return 2**x - 1


x = int(input())
for i in range(x):
    a, b = list(map(int, input().split(' ')))
    print(solve(a, b))
