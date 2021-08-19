def last_fib_digit(n):
    (a, b) = (0, 1)
    for _ in range(n % 60):
        (a, b) = (b, (b + a) % 10)
    return a
