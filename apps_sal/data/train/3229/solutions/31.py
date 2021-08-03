def am_i_wilson(n):
    return n == 5 or n == 13 or n == 563
    f = 1
    for i in range(2, n + 1):
        f *= i
    return False if n == 0 else not (f / (n * n) % 1).is_integer()
