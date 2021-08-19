def last_fib_digit(n):
    n = (n - 1) % 60
    (a, b) = (1, 1)
    for i in range(n):
        (a, b) = (b, (a + b) % 10)
    return a
