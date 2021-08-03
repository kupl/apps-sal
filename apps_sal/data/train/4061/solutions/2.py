def count_ones(n):
    a, ones = 7, 1
    for i in range(2, n + 1):
        b = a + gcd(i, a)
        if b == a + 1:
            ones += 1
        a = b

    return ones


def max_pn(n):
    a, p, i = 7, {1}, 1

    while len(p) < n + 1:
        i += 1
        b = a + gcd(i, a)
        p.add(b - a)
        a = b
    return max(p)


def an_over_average(n):
    return 3


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
