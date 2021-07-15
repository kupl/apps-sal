def hotpo(n):
    nof_times = 0
    while n != 1:
        n = 3 * n + 1 if n % 2 else n / 2
        nof_times += 1
    return nof_times
