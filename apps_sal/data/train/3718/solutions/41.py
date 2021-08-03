def divisors(n):
    y = 0
    for x in range(1, n + 1):
        if (n % x) == 0:
            y += 1
    return y
