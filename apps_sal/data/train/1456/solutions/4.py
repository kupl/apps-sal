from math import log2


def get_a(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return (n + 1) // 2 + get_a(n // 2) * 2


def get(n):
    if n < 1:
        return 0
    total = n * (n + 1) // 2
    a = get_a(n)
    return total - a - int(log2(n)) - 1


def read():
    t = int(input())
    for i in range(t):
        (l, r) = list(map(int, input().strip().split()))
        print(get(r) - get(l - 1))


read()
