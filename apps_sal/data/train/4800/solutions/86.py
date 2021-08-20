def hotpo(n):
    counter = 0
    while n != 1:
        n = 3 * n + 1 if n % 2 else n / 2
        counter += 1
    return counter
