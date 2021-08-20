def last_fib_digit(n):
    return int((5 ** 0.5 / 2 + 0.5) ** (n % 60) / 5 ** 0.5 + 0.5) % 10
