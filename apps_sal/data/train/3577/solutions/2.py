from collections import Counter


def fib_digits(n):
    a = 0
    b = 1
    for i in range(2, n + 1):
        (a, b) = (b, a + b)
    c = Counter(str(b))
    res = sorted([(int(x[0]), int(x[1])) for x in zip(list(c.values()), list(c.keys()))], key=lambda m: (m[0], m[1]))[::-1]
    return res
