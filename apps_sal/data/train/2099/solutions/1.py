import itertools
import math


def main():
    (n, k) = list(map(int, input().split()))
    a = 1
    b = n
    res = []
    for i in range(k - 1):
        if i % 2:
            res.append(a)
            a += 1
        else:
            res.append(b)
            b -= 1
    if k % 2:
        res += list(range(b, a - 1, -1))
    else:
        res += list(range(a, b + 1))
    print(' '.join(map(str, res)))


def __starting_point():
    main()


__starting_point()
