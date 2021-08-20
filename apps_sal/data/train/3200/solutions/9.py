from itertools import cycle


def thirt(n):
    m = -n
    while m != n:
        m = n
        n = sum((x * y for (x, y) in zip(cycle([1, 10, 9, 12, 3, 4]), map(int, str(n)[::-1]))))
    return n
