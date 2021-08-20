def fib_digits(n):
    d = str(fib(n))
    return sorted([(d.count(i), int(i)) for i in '0123456789' if d.count(i) > 0])[::-1]


def fib(n):
    (a, b) = (1, 1)
    for i in range(n - 1):
        (a, b) = (b, a + b)
    return a
