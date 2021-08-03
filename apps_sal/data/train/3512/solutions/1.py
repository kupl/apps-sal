def last_fib_digit(n):
    """ well, it is periodic on 60 """
    a = 0
    b = 1
    for _ in range(n % 60):
        a, b = b, (a + b) % 10
    return a
